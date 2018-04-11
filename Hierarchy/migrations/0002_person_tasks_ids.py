# Generated by Django 2.0.4 on 2018-04-11 13:28

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('Hierarchy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='tasks_ids',
            field=models.CharField(default='', max_length=200, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]