# Generated by Django 4.0.6 on 2022-07-25 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBackend', '0007_alter_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]
