# Generated by Django 5.0.6 on 2024-06-15 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_shoppingcart_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="image_url",
            field=models.URLField(default=""),
        ),
    ]
