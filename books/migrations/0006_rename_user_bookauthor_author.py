# Generated by Django 4.2.7 on 2023-11-28 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_bookreview_created_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookauthor',
            old_name='user',
            new_name='author',
        ),
    ]
