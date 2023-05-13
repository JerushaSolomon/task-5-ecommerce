# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-11 16:34
from __future__ import unicode_literals

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0031_basket'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopProductTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('short_description', models.CharField(blank=True, max_length=150, null=True, verbose_name='short description')),
            ],
            options={
                'verbose_name': 'shop product Translation',
                'db_table': 'shuup_shopproduct_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='shopproducttranslation',
            name='master',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.ShopProduct'),
        ),
        migrations.AlterUniqueTogether(
            name='shopproducttranslation',
            unique_together=set([('language_code', 'master')]),
        )
    ]
