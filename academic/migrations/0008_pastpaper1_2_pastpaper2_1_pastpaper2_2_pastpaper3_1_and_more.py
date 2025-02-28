# Generated by Django 5.0.6 on 2024-07-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0007_pastpaper1_1_course_yea1_sem1_pastpaper'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastPaper1_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PastPaper2_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PastPaper2_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PastPaper3_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PastPaper3_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PastPaper4_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PastPaper4_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='course',
            old_name='yea1_sem1_pastpaper',
            new_name='pastPaper1_1',
        ),
        migrations.AddField(
            model_name='course',
            name='pastPaper1_2',
            field=models.ManyToManyField(blank=True, to='academic.pastpaper1_2'),
        ),
        migrations.AddField(
            model_name='course',
            name='pastPaper2_1',
            field=models.ManyToManyField(blank=True, to='academic.pastpaper2_1'),
        ),
        migrations.AddField(
            model_name='course',
            name='pastPaper2_2',
            field=models.ManyToManyField(blank=True, to='academic.pastpaper2_2'),
        ),
        migrations.AddField(
            model_name='course',
            name='pastPaper3_1',
            field=models.ManyToManyField(blank=True, to='academic.pastpaper3_1'),
        ),
        migrations.AddField(
            model_name='course',
            name='pastPaper3_2',
            field=models.ManyToManyField(blank=True, to='academic.pastpaper3_2'),
        ),
        migrations.AddField(
            model_name='course',
            name='pastPaper4_1',
            field=models.ManyToManyField(blank=True, to='academic.pastpaper4_1'),
        ),
        migrations.AddField(
            model_name='course',
            name='pastPaper4_2',
            field=models.ManyToManyField(blank=True, to='academic.pastpaper4_2'),
        ),
    ]
