# Generated by Django 3.2.6 on 2021-08-11 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr1', models.TextField()),
                ('addr2', models.TextField()),
                ('postal', models.IntegerField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('country', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pan', models.TextField(max_length=12)),
                ('acc', models.IntegerField()),
                ('ifsc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromt', models.TimeField()),
                ('to', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('nationality', models.TextField()),
                ('Gender', models.TextField()),
                ('dob', models.DateField()),
                ('add', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.address')),
                ('creds', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Practitioner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('dp', models.ImageField(upload_to='media')),
                ('doj', models.DateField()),
                ('phone', models.IntegerField()),
                ('available', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.slot')),
                ('bank', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.bankaccount')),
                ('creds', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]