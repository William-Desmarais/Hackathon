# Generated by Django 4.2.10 on 2024-03-02 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='easyuser',
            name='goal_score',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='easyuser',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]