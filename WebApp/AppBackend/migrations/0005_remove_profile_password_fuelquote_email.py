# Generated by Django 4.0.6 on 2022-07-23 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBackend', '0004_fuelquote_remove_profile_id_profile_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
        migrations.AddField(
            model_name='fuelquote',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
