# Generated by Django 3.2.6 on 2021-09-20 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merlin', '0007_learninterface_prefix_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learninterface',
            name='prefix_length',
        ),
    ]
