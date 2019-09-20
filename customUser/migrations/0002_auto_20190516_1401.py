# Generated by Django 2.2.1 on 2019-05-16 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.BooleanField(choices=[(True, 'Male'), (False, 'Female')], verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='user',
            name='types',
            field=models.BooleanField(choices=[(True, 'Worker'), (False, 'Employer')], verbose_name='Sign as'),
        ),
    ]