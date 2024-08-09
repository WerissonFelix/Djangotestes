# Generated by Django 5.0.7 on 2024-08-03 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todos",
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
                ("title", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("deadline", models.DateTimeField()),
                ("finished_at", models.DateTimeField(null=True)),
            ],
        ),
    ]
