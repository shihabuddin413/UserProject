# Generated by Django 4.0.5 on 2022-08-06 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botmanager', '0006_rename_job_bot_admodel_job_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='botmanager',
            name='ManagerAdsIds',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
