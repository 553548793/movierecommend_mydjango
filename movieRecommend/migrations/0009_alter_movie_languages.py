# Generated by Django 3.2 on 2022-06-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieRecommend', '0008_alter_movie_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='languages',
            field=models.TextField(),
        ),
    ]