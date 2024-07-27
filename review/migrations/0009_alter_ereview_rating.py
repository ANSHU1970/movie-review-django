# Generated by Django 5.0.7 on 2024-07-25 17:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0008_alter_ereview_movies_series_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ereview",
            name="rating",
            field=models.CharField(
                choices=[
                    ("⭐", "⭐"),
                    ("⭐⭐", "⭐⭐"),
                    ("⭐⭐⭐", "⭐⭐⭐"),
                    ("⭐⭐⭐⭐", "⭐⭐⭐⭐"),
                    ("⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
                ],
                default="",
                max_length=8,
            ),
        ),
    ]
