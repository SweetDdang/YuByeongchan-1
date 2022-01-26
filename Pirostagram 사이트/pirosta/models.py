from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    like = models.IntegerField()


    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='게시글')
    content = models.TextField(verbose_name='댓글내용')
    
    
    def __str__(self):
        return self.content


