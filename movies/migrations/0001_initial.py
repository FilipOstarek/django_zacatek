# Generated by Django 3.1.2 on 2021-03-14 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a film genre (e.g. sci-fi, comedy)', max_length=50, unique=True, verbose_name='Genre name')),
            ],
        ),
    ]
