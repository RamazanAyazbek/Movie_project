# Generated by Django 4.2.1 on 2023-05-21 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_rename_descrition_category_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='country_en',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='country_ru',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='tagline_en',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='tagline_ru',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='movieshots',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='movieshots',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='movieshots',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='movieshots',
            name='title_ru',
        ),
    ]
