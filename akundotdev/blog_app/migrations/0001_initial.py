# Generated by Django 3.0.5 on 2020-04-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90, verbose_name='Title')),
                ('slug', models.SlugField(max_length=90, unique=True, verbose_name='Slug')),
                ('description', models.CharField(max_length=280, verbose_name='Description')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('content', models.TextField(help_text='Use Markdown syntax', verbose_name='Content')),
                ('views', models.IntegerField(default=0, verbose_name='Views')),
            ],
            options={
                'verbose_name': 'Article',
                'ordering': ['-created_on'],
            },
        ),
    ]
