# Generated by Django 5.0.4 on 2024-05-01 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka_name', models.CharField(max_length=16, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.category')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=32)),
                ('marka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.marka')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=32)),
                ('price', models.PositiveIntegerField(default=0)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('year', models.DateField(default=2024)),
                ('type', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='img/')),
                ('volume', models.FloatField(default=0.8)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.category')),
                ('marka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.marka')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.model')),
            ],
        ),
    ]
