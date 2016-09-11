# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-04 11:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import utils.model_functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArmArmour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('amount_of_items', models.DecimalField(decimal_places=0, max_digits=2)),
                ('health', models.DecimalField(decimal_places=0, max_digits=2)),
                ('value', models.DecimalField(decimal_places=0, max_digits=7)),
                ('battle_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='item.BattleItem')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
                ('item', models.ManyToManyField(blank=True, to='item.StandardItem')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, utils.model_functions.DetailURLMixin),
        ),
        migrations.CreateModel(
            name='BackPack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('amount_of_items', models.DecimalField(decimal_places=0, max_digits=2)),
                ('health', models.DecimalField(decimal_places=0, max_digits=2)),
                ('value', models.DecimalField(decimal_places=0, max_digits=7)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
                ('item', models.ManyToManyField(blank=True, to='item.StandardItem')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, utils.model_functions.DetailURLMixin),
        ),
        migrations.CreateModel(
            name='BodyArmour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('amount_of_items', models.DecimalField(decimal_places=0, max_digits=2)),
                ('health', models.DecimalField(decimal_places=0, max_digits=2)),
                ('value', models.DecimalField(decimal_places=0, max_digits=7)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
                ('item', models.ManyToManyField(blank=True, to='item.StandardItem')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, utils.model_functions.DetailURLMixin),
        ),
        migrations.CreateModel(
            name='HeadArmour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('amount_of_items', models.DecimalField(decimal_places=0, max_digits=2)),
                ('health', models.DecimalField(decimal_places=0, max_digits=2)),
                ('value', models.DecimalField(decimal_places=0, max_digits=7)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
                ('item', models.ManyToManyField(blank=True, to='item.StandardItem')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, utils.model_functions.DetailURLMixin),
        ),
        migrations.CreateModel(
            name='LegArmour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('amount_of_items', models.DecimalField(decimal_places=0, max_digits=2)),
                ('health', models.DecimalField(decimal_places=0, max_digits=2)),
                ('value', models.DecimalField(decimal_places=0, max_digits=7)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
                ('item', models.ManyToManyField(blank=True, to='item.StandardItem')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, utils.model_functions.DetailURLMixin),
        ),
    ]