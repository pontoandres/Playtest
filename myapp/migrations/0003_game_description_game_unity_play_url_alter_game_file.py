# Generated by Django 5.1.2 on 2024-10-13 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='game',
            name='unity_play_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='games/'),
        ),
    ]