# Generated by Django 3.2.6 on 2021-08-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20210811_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='practitioner',
            name='duration_in_mins',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitor',
            name='expectedOTP',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='visitor',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
