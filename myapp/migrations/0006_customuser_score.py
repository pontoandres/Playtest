# Generated by Django 5.1.2 on 2024-11-04 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
