from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    rating: int = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(3000)])
    DIGNITY_CHOICES: dict[str, str] = {
        'Fan': 'Fan',
        'CM': 'Candidate Master',
        'FM': 'FIDE Master',
        'IM': 'International Master',
        'GM': 'Grandmaster',
    }
    dignity: str = models.CharField(max_length=30, choices=DIGNITY_CHOICES)

    def __str__(self) -> str:
        return f'{self.username}'


class ChessCategory(models.Model):
    name: str = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'


class ChessPost(models.Model):
    title: str = models.CharField(max_length=200)
    content: str = models.TextField()
    publication_date: datetime = models.DateTimeField(auto_now_add=True)
    author: CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category: ChessCategory = models.ForeignKey(ChessCategory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title}'


class ChessComment(models.Model):
    post: ChessPost = models.ForeignKey(ChessPost, on_delete=models.CASCADE)
    author: CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content: str = models.TextField()
    publication_date: datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.author}'
