# Generated by Django 3.2.3 on 2022-04-15 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excerpts', '0009_alter_reward_reward_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='reward',
            name='ship_track',
            field=models.CharField(default='no shipping', max_length=64),
        ),
    ]
