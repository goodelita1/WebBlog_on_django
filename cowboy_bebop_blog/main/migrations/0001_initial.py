# Generated by Django 4.2.1 on 2023-05-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(max_length=50)),
                ("blog_header", models.CharField(max_length=50)),
                ("blog_text", models.TextField()),
                ("date", models.DateTimeField()),
            ],
            options={
                "ordering": ["blog_header"],
            },
        ),
    ]
