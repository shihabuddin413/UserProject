# Generated by Django 4.0.5 on 2022-08-06 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botmanager', '0008_submittedjobapplications_job_manger'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submittedjobapplications',
            old_name='job_manger',
            new_name='job_manager',
        ),
    ]