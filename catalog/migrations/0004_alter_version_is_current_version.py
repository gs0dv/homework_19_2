# Generated by Django 4.2.4 on 2023-08-23 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_current_version',
            field=models.BooleanField(default=True, verbose_name='признак текущей версии'),
        ),
    ]
