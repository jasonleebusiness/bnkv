# Generated by Django 3.1 on 2022-01-20 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='annuanl_income',
            new_name='annual_income',
        ),
    ]