# Generated by Django 5.1 on 2024-08-23 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=20)),
                ('jogo', models.CharField(blank=True, max_length=30, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('desc', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=20)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=64, unique=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=4)),
                ('desc', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='')),
                ('data_lancamento', models.DateField(blank=True, null=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='todos.empresas')),
            ],
        ),
        migrations.CreateModel(
            name='biblioteca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('id_jogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.jogo')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.usuario')),
            ],
        ),
    ]
