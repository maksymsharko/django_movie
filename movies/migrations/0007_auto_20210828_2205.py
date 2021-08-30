# Generated by Django 3.2.5 on 2021-08-28 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20210828_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='description_uk',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='name_uk',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_uk',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_uk',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='description_uk',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='name_uk',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='country_en',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='country_uk',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='description_uk',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='tagline_en',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='tagline_uk',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='title_uk',
        ),
        migrations.RemoveField(
            model_name='movieshots',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='movieshots',
            name='description_uk',
        ),
        migrations.RemoveField(
            model_name='movieshots',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='movieshots',
            name='title_uk',
        ),
    ]
