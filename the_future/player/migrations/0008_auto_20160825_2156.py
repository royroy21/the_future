# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-25 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0007_auto_20160825_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armarmour',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='armarmour',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='backpack',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='backpack',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='battleitem',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='battleitem',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='bodyarmour',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='bodyarmour',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='faction',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='faction',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='head',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='head',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='item',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='item',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='legarmour',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='legarmour',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='player',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='player',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.Account'),
        ),
    ]