# Generated by Django 5.0.7 on 2024-08-08 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0002_rename_todos_todo"),
    ]

    operations = [
        migrations.CreateModel(
            name="alunos",
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
                ("name", models.CharField(max_length=100)),
                ("ano", models.DateTimeField(auto_now=True)),
                ("idade", models.DateTimeField()),
                ("matricula", models.DateTimeField(null=True)),
            ],
        ),
    ]
