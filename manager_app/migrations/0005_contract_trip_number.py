# Generated by Django 2.2.10 on 2020-04-29 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0004_auto_20200428_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='trip_number',
            field=models.CharField(max_length=45, null=True),
        ),
    ]