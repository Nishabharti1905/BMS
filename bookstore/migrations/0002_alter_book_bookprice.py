# Generated by Django 4.2.8 on 2023-12-28 06:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookstore", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="bookprice",
            field=models.IntegerField(default=0),
        ),
    ]
