# Generated by Django 5.0.7 on 2024-07-25 13:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0003_alter_review_movies_series_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="rating",
            field=models.CharField(
                choices=[
                    ("terrible", "⭐"),
                    ("bad", "⭐⭐"),
                    ("ok ok", "⭐⭐⭐"),
                    ("good", "⭐⭐⭐⭐"),
                    ("best", "⭐⭐⭐⭐"),
                ],
                default=" ",
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="movies_series_name",
            field=models.CharField(default="Movie or Series Name", max_length=50),
        ),
    ]
