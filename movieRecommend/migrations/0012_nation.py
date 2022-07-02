# Generated by Django 3.2 on 2022-06-30 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieRecommend', '0011_alter_directors_directors'),
    ]

    operations = [
        migrations.CreateModel(
            name='nation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nation', models.CharField(max_length=20)),
                ('movieid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieRecommend.movie')),
            ],
        ),
    ]
