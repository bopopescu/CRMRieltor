# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('setting_street', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
        ('arendator', '0020_auto_20160802_0233'),
        ('facility', '0003_auto_20160802_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commission', models.CharField(max_length=10, null=True, verbose_name='\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f', blank=True)),
                ('name', models.CharField(max_length=250, verbose_name='\u0418\u043c\u044f', blank=True)),
                ('phone_first', models.IntegerField(null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d - 1', blank=True)),
                ('phone_second', models.IntegerField(null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d - 2', blank=True)),
                ('comment', models.TextField(null=True, verbose_name='\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='\u0415\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430', blank=True)),
                ('rooms_from', models.IntegerField(null=True, verbose_name='\u041a\u043e\u043c\u043d\u0430\u0442 \u041e\u0442', blank=True)),
                ('rooms_to', models.IntegerField(null=True, verbose_name='\u041a\u043e\u043c\u043d\u0430\u0442 \u0414\u043e', blank=True)),
                ('floors_from', models.IntegerField(null=True, verbose_name='\u042d\u0442\u0430\u0436\u043d\u043e\u0441\u0442\u044c \u041e\u0442', blank=True)),
                ('floors_to', models.IntegerField(null=True, verbose_name='\u042d\u0442\u0430\u0436\u043d\u043e\u0441\u0442\u044c \u0414\u043e', blank=True)),
                ('area_from', models.IntegerField(null=True, verbose_name='\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u041e\u0442', blank=True)),
                ('area_to', models.IntegerField(null=True, verbose_name='\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u0414\u043e', blank=True)),
                ('price_from', models.IntegerField(null=True, verbose_name='\u0426\u0435\u043d\u0430 \u041e\u0442', blank=True)),
                ('price_to', models.IntegerField(null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0414\u043e', blank=True)),
                ('date_term', models.DateField(null=True, verbose_name='\u0421\u0440\u043e\u043a\u0438', blank=True)),
                ('review_date', models.DateField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f', null=True)),
                ('call_date', models.DateField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0432\u043e\u043d\u043a\u0430', blank=True)),
                ('time_trash', models.DateTimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f', blank=True)),
                ('name_user_trash', models.CharField(max_length=100, null=True, verbose_name='\u041a\u0442\u043e \u0443\u0434\u0430\u043b\u0438\u043b', blank=True)),
                ('trash', models.BooleanField(default=False, verbose_name='\u041a\u043e\u0440\u0437\u0438\u043d\u0430')),
                ('district_obj', models.ManyToManyField(related_name='districts_b', verbose_name='\u0420\u0430\u0439\u043e\u043d', to='setting_street.District', blank=True)),
            ],
            options={
                'verbose_name': '\u041f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u041f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u0438',
            },
        ),
        migrations.CreateModel(
            name='UserFullName',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='buyer',
            name='loyality',
            field=models.ManyToManyField(related_name='loyal_b', verbose_name='\u041b\u043e\u044f\u043b\u044c\u043d\u043e\u0441\u0442\u044c', to='buyer.UserFullName', blank=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='number_of_persons',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a', blank=True, to='facility.TypeNumberOfPerson', null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='repairs',
            field=models.ManyToManyField(to='facility.TypeRepairs', verbose_name='\u0420\u0435\u043c\u043e\u043d\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='rieltor',
            field=models.ManyToManyField(related_name='rielt_b', verbose_name='\u0420\u0438\u0435\u043b\u0442\u043e\u0440', to='buyer.UserFullName', blank=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='room',
            field=models.ManyToManyField(to='facility.TypeRooms', verbose_name='\u041a\u043e\u043c\u043d\u0430\u0442\u044b', blank=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='type_building_data',
            field=models.ManyToManyField(to='facility.TypeFacility', verbose_name='\u0422\u0438\u043f \u043e\u0431\u044a\u0435\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='type_client',
            field=models.ForeignKey(related_name='t_client_b', blank=True, to='arendator.TypeClient', null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='type_stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u042d\u0442\u0430\u043f', blank=True, to='arendator.TypeStage', null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='type_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435', blank=True, to='arendator.TypeState', null=True),
        ),
    ]