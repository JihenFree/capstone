# Generated by Django 3.2.3 on 2022-04-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excerpts', '0010_reward_ship_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
    ]
