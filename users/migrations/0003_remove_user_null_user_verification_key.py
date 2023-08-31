# Generated by Django 4.2.4 on 2023-08-31 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_null'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='null',
        ),
        migrations.AddField(
            model_name='user',
            name='verification_key',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='ключ'),
        ),
    ]
