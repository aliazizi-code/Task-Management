from django.core.validators import RegexValidator
from django.db import models


class Tag(models.Model):
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9_]+$',
        message='Tag name must consist of letters, numbers, and underscores only.'
    )

    name = models.CharField(
        max_length=50,
        validators=[name_validator],
        unique=True
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.TextChoices):
        in_progress = 'InProgress'
        complete = 'Complete'
        cancelled = 'Cancelled'

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(choices=Status.choices, default=Status.in_progress, max_length=100)
    tags = models.ManyToManyField(Tag, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
