# Generated by Django 4.2.6 on 2023-11-04 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_screener_cash_clause_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='screener',
            name='cash_clause',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='screener',
            name='future_clause',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='screener',
            name='nifty_clause',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
