# Generated by Django 2.0.4 on 2018-08-24 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InnovationHubWebsite', '0008_auto_20180727_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='colour',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
