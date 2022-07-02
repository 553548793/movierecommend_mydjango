from django.db import models

# Create your models here.



class movie(models.Model):
    movieid = models.IntegerField(primary_key=True, unique=True, null=False)
    moviename = models.CharField(max_length= 100)
    rating = models.FloatField()
    poster = models.CharField(max_length= 200)
    languages = models.TextField()
    year = models.IntegerField()
    summary = models.TextField()
    duration = models.CharField(max_length= 200)
    rating_people = models.IntegerField()
    percentage5 = models.FloatField()
    percentage4 = models.FloatField()
    percentage3 = models.FloatField()
    percentage2 = models.FloatField()
    percentage1 = models.FloatField()

class user_rating(models.Model):
    userid = models.AutoField(primary_key=True)
    movieid = models.ForeignKey(to=movie, to_field='movieid', on_delete=models.CASCADE)
    rating = models.FloatField()
    timestamp = models.CharField(max_length= 10)

class genre(models.Model):
    movieid = models.ForeignKey(to=movie, to_field='movieid', on_delete=models.CASCADE)
    genres = models.CharField(max_length= 20)

class directors(models.Model):
    movieid = models.ForeignKey(to=movie, to_field="movieid", on_delete=models.CASCADE)
    directors = models.CharField(max_length= 200)

class casts(models.Model):
    movieid = models.ForeignKey(to=movie, to_field='movieid', on_delete=models.CASCADE)
    casts = models.CharField(max_length= 200)

class comments(models.Model):
    movieid = models.ForeignKey(to=movie, to_field='movieid', on_delete=models.CASCADE)
    comments_name = models.CharField(max_length= 50)
    comments_txt = models.TextField()
    rating = models.FloatField()

class nation(models.Model):
    movieid = models.ForeignKey(to=movie, to_field='movieid', on_delete=models.CASCADE)
    nation = models.CharField(max_length= 20)