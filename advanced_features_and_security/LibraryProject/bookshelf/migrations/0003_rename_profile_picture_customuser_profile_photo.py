# Generated by Django 5.1 on 2024-08-21 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_alter_customuser_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='profile_picture',
            new_name='profile_photo',
        ),
    ]
