# Generated by Django 3.1 on 2022-06-07 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20220606_1609'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SwiftCode',
        ),
        migrations.DeleteModel(
            name='TaxCode',
        ),
    ]
