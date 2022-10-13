# Generated by Django 4.1.1 on 2022-09-28 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_alter_ratting_movie"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(
                related_name="film_actor", to="movies.actor", verbose_name="Актеры"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="directors",
            field=models.ManyToManyField(
                related_name="film_director", to="movies.actor", verbose_name="Режиссер"
            ),
        ),
    ]
