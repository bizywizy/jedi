# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 15:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Jedi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            managers=[
                ('can_teach', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('right_answer', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='jedi',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedi.Planet'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jedi.Planet'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='question',
            field=models.ManyToManyField(to='jedi.Question'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='jedi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jedi.Jedi'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedi.Planet'),
        ),
        migrations.AddField(
            model_name='answer',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedi.Candidate'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedi.Question'),
        ),
    ]
