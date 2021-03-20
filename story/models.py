from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    Name=models.CharField(max_length=50)
    Username=models.CharField(max_length=30,unique=True)
    Password=models.CharField(max_length=50)

    def __str__(self):
        return self.Username

class Story(models.Model):
    category_choices=[
        ('pol','politics'),
        ('art','art_news'),
        ('tech','technology_new'),
        ('trivia','trivial_news')
    ]
    region_choices=[
        ('uk','United_Kingdom_news'),
        ('eu','European_news'),
        ('w','world_news'),
    ]
    Story_Headline=models.CharField(max_length=64)
    Story_Category=models.CharField(max_length=6,choices=category_choices,default='trivia')
    Story_Region=models.CharField(max_length=2,choices=region_choices,default='uk')
    # Post_Date=models.DateTimeField(default=timezone.now)
    Post_Date=models.DateTimeField(auto_now_add=True)
    Story_Details=models.CharField(max_length=512)
    Authors=models.ManyToManyField(Author)

    def __str__(self):
        return self.Story_Headline