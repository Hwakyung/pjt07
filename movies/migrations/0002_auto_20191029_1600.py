# Generated by Django 2.2.4 on 2019-10-29 07:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genres',
            new_name='Genre',
        ),
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]
