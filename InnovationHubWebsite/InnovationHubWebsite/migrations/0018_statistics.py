# Generated by Django 2.0.4 on 2018-12-17 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InnovationHubWebsite', '0017_remove_featuredprint_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_name', models.CharField(max_length=30)),
                ('print_num', models.IntegerField()),
                ('print_time_average', models.IntegerField()),
                ('wait_time_average', models.IntegerField()),
                ('successful_submission_num', models.IntegerField()),
                ('failed_submission_num', models.IntegerField()),
            ],
        ),
    ]
