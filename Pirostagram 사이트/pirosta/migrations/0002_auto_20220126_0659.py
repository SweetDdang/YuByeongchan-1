# Generated by Django 3.1.8 on 2022-01-26 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pirosta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
