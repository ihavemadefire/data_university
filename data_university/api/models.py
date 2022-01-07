from django.db import models

# Create your models here.

class Presenter(models.Model):
    name = models.CharField(max_length=75)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=75)
    def __str__(self):
        return self.name

class Session(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=300, null=True)
    presenter = models.ManyToManyField(Presenter)
    tags = models.ManyToManyField(Tag)
    video_link = models.URLField(max_length=250)
    date_recorded = models.DateField(auto_now=False)
    date_added = models.DateField(auto_now=True)
    DIFFICULTY = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    difficulty = models.CharField(max_length=50, choices= DIFFICULTY)
    slug = models.SlugField(blank=True, unique=True)
    def __str__(self):
        return self.title
