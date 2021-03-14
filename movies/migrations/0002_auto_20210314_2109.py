# Generated by Django 3.1.2 on 2021-03-14 20:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('plot', models.TextField(blank=True, null=True, verbose_name='Plot')),
                ('release_date', models.DateField(blank=True, help_text='Please use the following format: <em>YYYYMM-DD</em>.', null=True, verbose_name='Release date')),
                ('runtime', models.IntegerField(blank=True, help_text='Please enter an integer value (minutes)', null=True, verbose_name='Runtime')),
                ('rate', models.FloatField(default=5.0, help_text='Please enter an float value (range 1.0 - 10.0)', null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='Rate')),
                ('genres', models.ManyToManyField(help_text='Select a genre for this film', to='movies.Genre')),
            ],
            options={
                'ordering': ['-release_date', 'title'],
            },
        ),
    ]
