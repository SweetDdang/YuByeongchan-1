from django.db import models

class Post(models.Model):
    title = models.CharField(verbose_name="제목", max_length=200)
    created_date = models.IntegerField(verbose_name="개봉년도",max_length=4)
    genre = models.CharField(verbose_name="장르",max_length=200)
    star = models.FloatField(verbose_name="별점",max_length=3)
    running_time = models.IntegerField(verbose_name="러닝타임")
    text = models.TextField(verbose_name="리뷰")
    director = models.CharField(verbose_name="감독",max_length=200)
    actor = models.CharField(verbose_name="배우",max_length=200)
    
    def __str__(self):
        return self.title