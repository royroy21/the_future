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
        ('armour', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, utils.model_functions.DetailURLMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('melee', models.DecimalField(decimal_places=0, max_digits=1)),
                ('ballistic', models.DecimalField(decimal_places=0, max_digits=1)),
                ('strength', models.DecimalField(decimal_places=0, max_digits=1)),
                ('toughness', models.DecimalField(decimal_places=0, max_digits=1)),
                ('wounds', models.DecimalField(decimal_places=0, max_digits=1)),
                ('initiative', models.DecimalField(decimal_places=0, max_digits=1)),
                ('attacks', models.DecimalField(decimal_places=0, max_digits=1)),
                ('leadership', models.DecimalField(decimal_places=0, max_digits=1)),
                ('health', models.DecimalField(decimal_places=0, max_digits=1)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
                ('backpack', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='armour.BackPack')),
                ('body', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='armour.BodyArmour')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
                ('faction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='player.Faction')),
                ('head', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='armour.HeadArmour')),
                ('left_arm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='left_arm', to='armour.ArmArmour')),
                ('left_leg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='left_leg', to='armour.LegArmour')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account')),
                ('right_arm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='right_arm', to='armour.ArmArmour')),
                ('right_leg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='right_leg', to='armour.LegArmour')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, utils.model_functions.DetailURLMixin),
        ),
    ]
