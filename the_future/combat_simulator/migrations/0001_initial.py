# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-11 22:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import utils.model_functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('hero', '0001_initial'),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CombatRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
                ('initiating_hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.Hero')),
                ('initiating_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.Player')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
                ('waiting_for_hero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='waiting_for_hero', to='hero.Hero')),
                ('waiting_for_player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='waiting_for_player', to='player.Player')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, utils.model_functions.DetailURLMixin),
        ),
    ]