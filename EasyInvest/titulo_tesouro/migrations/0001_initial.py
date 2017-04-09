# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='titulo_tesouro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('categoria_titulo', models.CharField(max_length=58)),
                ('mes', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('acao', models.CharField(max_length=7)),
                ('valor', models.FloatField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]