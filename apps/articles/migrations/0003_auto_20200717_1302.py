# Generated by Django 3.0.8 on 2020-07-17 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_source_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['tag_name'], 'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
    ]