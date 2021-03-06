# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import arendator.models


class Migration(migrations.Migration):

    dependencies = [
        ('arendator', '0005_auto_20161005_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arendator',
            name='name',
            field=models.CharField(max_length=250, null=True, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='arendator',
            name='phone_first',
            field=models.CharField(max_length=15, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d - 1', validators=[arendator.models.validate_isnumber]),
        ),
        migrations.AlterField(
            model_name='arendator',
            name='phone_second',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d - 2', validators=[arendator.models.validate_isnumber]),
        ),
        migrations.AlterField(
            model_name='arendator',
            name='room',
            field=models.ManyToManyField(to='facility.TypeRooms', verbose_name='\u041a\u043e\u043c\u043d\u0430\u0442\u044b'),
        ),
    ]
