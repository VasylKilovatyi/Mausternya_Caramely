# Generated by Django 5.0.2 on 2024-03-27 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_image_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_thumbnail',
        ),
    ]
