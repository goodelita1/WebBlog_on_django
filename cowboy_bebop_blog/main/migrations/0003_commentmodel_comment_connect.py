# Generated by Django 4.2.1 on 2023-05-18 16:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_commentmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="commentmodel",
            name="comment_connect",
            field=models.ManyToManyField(null=True, to="main.blogmodel"),
        ),
    ]
