# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 21:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jedi', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([('candidate', 'question')]),
        ),
    ]