# Generated by Django 4.2.6 on 2023-10-18 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_subscription_ends_transactions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='subscription_ends',
        ),
    ]
