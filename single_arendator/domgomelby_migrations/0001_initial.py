# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arendator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleArendatorComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9')),
                ('date_comment', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u043a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f')),
                ('author_comment', models.CharField(max_length=100, verbose_name='\u0410\u0432\u0442\u043e\u0440 \u043a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f')),
                ('image', models.CharField(default=b'0', max_length=100)),
                ('type_tabs', models.CharField(max_length=20, verbose_name='\u041a\u0430\u043a\u0430\u044f \u0432\u043a\u043b\u0430\u0434\u043a\u0430?')),
                ('obj_comments', models.ForeignKey(verbose_name='\u041e\u0431\u044c\u0435\u043a\u0442', to='arendator.Arendator')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043e\u0431\u0435\u043a\u0442\u0430',
                'verbose_name_plural': '\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432',
            },
        ),
    ]
