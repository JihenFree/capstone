# Generated by Django 3.2.3 on 2022-03-23 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excerpts', '0006_topbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='no address added yet', max_length=255),
        ),
    ]
