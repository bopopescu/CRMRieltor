# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0024_auto_20160710_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressfacilitydata',
            name='sleeps',
            field=models.IntegerField(null=True, verbose_name='\u0421\u043f\u0430\u043b\u044c\u043d\u044b\u0445 \u043c\u0435\u0441\u0442', blank=True),
        ),
    ]
