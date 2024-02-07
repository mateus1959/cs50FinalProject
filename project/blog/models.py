from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200) 
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    likes = models.IntegerField(default=0) # How many people endorse that book.

    def __str__(self):
        return f"\"{self.title}\""


class Post(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE) # Foreign key to hold the book ID of the book this post is about
    name = models.CharField(max_length=50) # Username of the user who read the book
    date = models.DateField("date posted") # Date on which user posted

    def __str__(self):
        return f"{self.date} - {self.name}: {self.book}"