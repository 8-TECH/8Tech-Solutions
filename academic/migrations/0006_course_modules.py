# Generated by Django 5.0.6 on 2024-07-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0005_notes_remove_course_notes_course_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='modules',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
