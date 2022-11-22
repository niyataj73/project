# Generated by Django 4.1.2 on 2022-11-04 09:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='image')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('Create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('p', 'Publish')], max_length=1)),
            ],
        ),
    ]
