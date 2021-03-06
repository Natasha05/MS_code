# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-14 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlphaTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experimentName', models.TextField(max_length=128, unique=True)),
                ('description', models.TextField(null=True)),
                ('resultId', models.TextField()),
                ('fileNames', models.TextField()),
                ('pca', models.TextField(null=True)),
                ('hclus', models.TextField(null=True)),
                ('heatmap', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultId', models.TextField()),
                ('fileName', models.TextField()),
                ('category', models.TextField(null=True)),
                ('motif_count', models.IntegerField(default=300, null=True)),
                ('experimentName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decomp.Experiment')),
            ],
        ),
        migrations.CreateModel(
            name='MotifList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MotifName', models.TextField()),
                ('MotifId', models.IntegerField(default=1)),
                ('Annotation', models.TextField(null=True)),
                ('z_score', models.FloatField(null=True)),
                ('t_value', models.FloatField(null=True)),
                ('p_value', models.FloatField(null=True)),
                ('experimentName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decomp.Experiment')),
            ],
        ),
        migrations.CreateModel(
            name='MotifSetList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motifset', models.TextField(default=1, max_length=128, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='experiment',
            name='motifset',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='decomp.MotifSetList'),
        ),
        migrations.AddField(
            model_name='alphatable',
            name='fileName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decomp.FileDetail'),
        ),
        migrations.AddField(
            model_name='alphatable',
            name='mass2motif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decomp.MotifList'),
        ),
    ]
