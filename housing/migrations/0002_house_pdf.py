# Generated by Django 5.0.6 on 2024-07-19 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
    ]
