# Generated by Django 4.2.7 on 2023-11-28 12:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_bookreview_created_time_alter_bookreview_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
