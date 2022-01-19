from code import interact
from django.db import models

class Dev_tool(models.Model):
    name = models.CharField(verbose_name='틀 이름',max_length=30)
    kind = models.CharField(verbose_name='틀 종류',max_length=30)
    description = models.TextField(verbose_name='개발 툴 설명')

    def __str__(self):
        return self.name


class Idea(models.Model):
    title = models.CharField(verbose_name="아이디어명", max_length=50)
    image = models.ImageField(verbose_name='대표사진', upload_to="", null=True)
    content = models.TextField(verbose_name="아이디어 설명")
    interest = models.IntegerField(verbose_name="아이디어 관심도", default=0)
    devtool = models.ForeignKey(Dev_tool, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title



