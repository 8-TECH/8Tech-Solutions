# Generated by Django 5.0.6 on 2024-07-16 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_news_scrol_remove_slide_name_remove_slide_news_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrol',
            name='topic',
            field=models.CharField(blank=True, default='Latest News', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='slide',
            name='slide_topic',
            field=models.CharField(blank=True, default='Latest News', max_length=200, null=True),
        ),
    ]
