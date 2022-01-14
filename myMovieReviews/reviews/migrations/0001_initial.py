# Generated by Django 4.0.1 on 2022-01-14 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.IntegerField(max_length=4)),
                ('genre', models.CharField(max_length=200)),
                ('star', models.FloatField(max_length=3)),
                ('running_time', models.IntegerField()),
                ('text', models.TextField()),
                ('director', models.CharField(max_length=200)),
                ('actor', models.CharField(max_length=200)),
            ],
        ),
    ]
