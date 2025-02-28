# Generated by Django 5.0.6 on 2024-07-15 06:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('scrol_images', models.ImageField(blank=True, default='default.jpeg', null=True, upload_to='')),
                ('topic', models.CharField(blank=True, max_length=200, null=True)),
                ('news_images', models.ImageField(blank=True, default='default.jpeg', null=True, upload_to='')),
                ('news_topic', models.CharField(blank=True, max_length=200, null=True)),
                ('news_description', models.TextField(blank=True, max_length=200, null=True)),
                ('admin_name', models.CharField(blank=True, max_length=200, null=True)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('video', models.TextField(blank=True, max_length=1000, null=True)),
                ('auto_video', models.TextField(blank=True, max_length=1000, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('slide_image', models.ImageField(blank=True, default='default.jpeg', null=True, upload_to='')),
                ('slide_topic', models.CharField(blank=True, max_length=200, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
