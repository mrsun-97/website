# Generated by Django 2.0.2 on 2018-04-07 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=40)),
                ('timestamp', models.CharField(max_length=15)),
                ('introduction', models.TextField()),
                ('image', models.CharField(max_length=40)),
                ('url', models.URLField()),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=40)),
                ('timestamp', models.CharField(max_length=15)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=150)),
                ('image1', models.CharField(max_length=40)),
                ('image2', models.CharField(max_length=40)),
                ('url', models.URLField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField()),
                ('style', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('introduction', models.TextField()),
                ('image', models.CharField(max_length=100)),
                ('host', models.CharField(max_length=10)),
                ('sub', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
