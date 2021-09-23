# Generated by Django 3.2.6 on 2021-09-22 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merlin', '0015_auto_20210922_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearnConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pyats_alias', models.TextField()),
                ('os', models.TextField()),
                ('config', models.JSONField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]