# Generated by Django 3.2.6 on 2021-08-12 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timing', models.TimeField()),
                ('date', models.DateField()),
                ('practitioner', models.ManyToManyField(to='authentication.Practitioner')),
                ('visitor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.visitor')),
            ],
        ),
    ]
