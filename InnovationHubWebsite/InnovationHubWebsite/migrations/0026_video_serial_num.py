# Generated by Django 2.0.4 on 2018-12-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InnovationHubWebsite', '0025_auto_20181222_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='serial_num',
            field=models.IntegerField(null=True),
        ),
    ]
