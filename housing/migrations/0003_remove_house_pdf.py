# Generated by Django 5.0.6 on 2024-07-19 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_house_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='pdf',
        ),
    ]
