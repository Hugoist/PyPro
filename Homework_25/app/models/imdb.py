from django.contrib.auth.models import User
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {"id": self.id, "name": self.name}


class Movie(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        agg = self.reviews.aggregate(avg=models.Avg("score"))
        avg = agg.get("avg") or None
        if avg is not None:
            return float(round(avg, 2))
        return None

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "release_date": self.release_date,
            "genres": [g.name for g in self.genres.all()],
            "average_rating": self.average_rating,
            "created_at": self.created_at,
        }


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movie_reviews")
    text = models.TextField(blank=True, null=True)
    score = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("movie", "user")

    def __str__(self):
        return f"Review {self.id} by {self.user.username} for {self.movie.title}"

    def to_dict(self):
        return {
            "id": self.id,
            "movie_id": self.movie_id,
            "user_id": self.user_id,
            "username": self.user.username,
            "text": self.text,
            "score": self.score,
            "created_at": self.created_at,
        }
