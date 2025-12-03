from enum import Enum
from typing import List

from django.db.models import Avg
from django.shortcuts import get_object_or_404
from ninja import Router, Query

from app.api.auth import auth
from app.models.imdb import Movie, Genre, Review
from app.schemas.imdb import (
    GenreCreateSchema, GenreReadSchema,
    MovieCreateSchema, MovieUpdateSchema, MovieReadSchema,
    ReviewCreateSchema, ReviewReadSchema,
)

router = Router(tags=["IMDb"])


# GENRES
@router.post("/genres", auth=auth, response=GenreReadSchema)
def create_genre(request, data: GenreCreateSchema):
    obj, created = Genre.objects.get_or_create(name=data.name.strip())
    return obj


@router.get("/genres", response=List[GenreReadSchema])
def list_genres(request):
    return Genre.objects.all()


# MOVIES CRUD + FILTER/SEARCH

class MovieOrderEnum(str, Enum):
    title = "title"
    release_date = "release_date"
    created_at = "created_at"
    average_rating = "average_rating"


@router.post("/movies", auth=auth, response=MovieReadSchema)
def create_movie(request, data: MovieCreateSchema):
    movie = Movie.objects.create(
        title=data.title,
        description=data.description,
        release_date=data.release_date,
    )
    if data.genre_ids:
        genres = Genre.objects.filter(id__in=data.genre_ids)
        movie.genres.set(genres)
    return movie.to_dict()


@router.get("/movies", response=List[MovieReadSchema])
def list_movies(
        request,
        genre: int | None = Query(None, description="Filter by genre id"),
        min_rating: float | None = Query(None, description="Minimum average rating"),
        release_from: str | None = Query(None, description="Release date from (YYYY-MM-DD)"),
        release_to: str | None = Query(None, description="Release date to (YYYY-MM-DD)"),
        search: str | None = Query(None, description="Partial title search"),
        order_by: MovieOrderEnum = Query(MovieOrderEnum.created_at),
):
    qs = Movie.objects.all().prefetch_related("genres")

    if genre is not None:
        qs = qs.filter(genres__id=genre)

    if search:
        qs = qs.filter(title__icontains=search)

    if release_from:
        qs = qs.filter(release_date__gte=release_from)
    if release_to:
        qs = qs.filter(release_date__lte=release_to)

    # annotate to avoid property conflict
    qs = qs.annotate(avg_rating=Avg("reviews__score"))

    if min_rating is not None:
        qs = qs.filter(avg_rating__gte=min_rating)

    order_value = order_by.value
    direction = ""
    if order_by.startswith("-"):
        direction = "-"
        field = order_value[1:]
    else:
        field = order_value

    if field == "average_rating":
        qs = qs.order_by(f"{direction}avg_rating")
    else:
        qs = qs.order_by(f"{direction}{field}")

    result = []
    for movie in qs:
        avg = getattr(movie, "avg_rating", None)
        if avg is None:
            avg = movie.average_rating
        movie_dict = movie.to_dict()
        movie_dict["average_rating"] = float(avg) if avg is not None else None
        result.append(movie_dict)

    return result


@router.get("/movies/{movie_id}", response=MovieReadSchema)
def get_movie(request, movie_id: int):
    movie = get_object_or_404(Movie.objects.prefetch_related("genres"), id=movie_id)
    return movie.to_dict()


@router.put("/movies/{movie_id}", auth=auth, response=MovieReadSchema)
def update_movie(request, movie_id: int, data: MovieUpdateSchema):
    movie = get_object_or_404(Movie, id=movie_id)
    payload = {k: v for k, v in data.dict().items() if v is not None}

    if "title" in payload:
        movie.title = payload["title"]
    if "description" in payload:
        movie.description = payload["description"]
    if "release_date" in payload:
        movie.release_date = payload["release_date"]
    movie.save()

    if data.genre_ids is not None:
        genres = Genre.objects.filter(id__in=data.genre_ids)
        movie.genres.set(genres)
    return movie.to_dict()


@router.delete("/movies/{movie_id}", auth=auth)
def delete_movie(request, movie_id: int):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return {"success": True}


# REVIEWS
@router.post("/reviews", auth=auth, response=ReviewReadSchema)
def create_review(request, data: ReviewCreateSchema):
    movie = get_object_or_404(Movie, id=data.movie_id)

    # update if exists (one review per user per movie)
    review, created = Review.objects.update_or_create(
        movie=movie,
        user=request.user,
        defaults={"text": data.text, "score": data.score},
    )
    return review.to_dict()


@router.get("/movies/{movie_id}/reviews", response=List[ReviewReadSchema])
def list_reviews(request, movie_id: int):
    movie = get_object_or_404(Movie, id=movie_id)
    qs = movie.reviews.select_related("user").order_by("-created_at")
    return [r.to_dict() for r in qs]
