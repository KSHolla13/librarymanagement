# Generated by Django 3.2 on 2022-06-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('published', models.CharField(max_length=25)),
            ],
        ),
    ]