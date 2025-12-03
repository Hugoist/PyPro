from typing import List

from django.shortcuts import get_object_or_404
from django.utils import timezone
from ninja import Router

from app.api.auth import auth
from app.models.library import Book, Author, BookGenre, Rental
from app.schemas.library import (
    BookCreateSchema, BookUpdateSchema, BookReadSchema,
    GenreSchema, AuthorSchema,
    RentalCreateSchema, RentalReadSchema,
)

router = Router(tags=["Library"])


# GENRES
@router.get("/genres", response=List[GenreSchema])
def list_genres(request):
    return BookGenre.objects.all()


# AUTHORS
@router.get("/authors", response=List[AuthorSchema])
def list_authors(request):
    return Author.objects.all()


# BOOKS
@router.post("/books", auth=auth, response=BookReadSchema)
def create_book(request, data: BookCreateSchema):
    book = Book.objects.create(
        title=data.title,
        description=data.description,
        available_copies=data.available_copies
    )
    if data.genre_ids:
        book.genres.set(BookGenre.objects.filter(id__in=data.genre_ids))
    if data.author_ids:
        book.authors.set(Author.objects.filter(id__in=data.author_ids))
    return book


@router.get("/books", response=List[BookReadSchema])
def list_books(
        request,
        title: str | None = None,
        author: str | None = None,
        genre: str | None = None,
):
    qs = Book.objects.prefetch_related("authors", "genres")

    if title:
        qs = qs.filter(title__icontains=title.strip())

    if author:
        qs = qs.filter(authors__name__icontains=author.strip())

    if genre:
        qs = qs.filter(genres__name__icontains=genre.strip())

    return qs.distinct()


@router.get("/books/{book_id}", response=BookReadSchema)
def get_book(request, book_id: int):
    return get_object_or_404(Book.objects.prefetch_related("genres", "authors"), id=book_id)


@router.put("/books/{book_id}", auth=auth, response=BookReadSchema)
def update_book(request, book_id: int, data: BookUpdateSchema):
    book = get_object_or_404(Book, id=book_id)
    payload = {k: v for k, v in data.dict().items() if v is not None}

    for field in ["title", "description", "available_copies"]:
        if field in payload:
            setattr(book, field, payload[field])

    book.save()

    if data.genre_ids is not None:
        book.genres.set(BookGenre.objects.filter(id__in=data.genre_ids))
    if data.author_ids is not None:
        book.authors.set(Author.objects.filter(id__in=data.author_ids))

    return book


@router.delete("/books/{book_id}", auth=auth)
def delete_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return {"success": True}


# RENTALS
@router.post("/rentals", auth=auth, response=RentalReadSchema)
def rent_book(request, data: RentalCreateSchema):
    book = get_object_or_404(Book, id=data.book_id)
    if book.available_copies < 1:
        return {"error": "No available copies"}
    rental = Rental.objects.create(user=request.user, book=book)
    book.available_copies -= 1
    book.save()
    return rental


@router.post("/rentals/{rental_id}/return", auth=auth, response=RentalReadSchema)
def return_book(request, rental_id: int):
    rental = get_object_or_404(Rental, id=rental_id, returned_at__isnull=True)
    rental.returned_at = timezone.now()
    rental.save()
    rental.book.available_copies += 1
    rental.book.save()
    return rental
