# Generated by Django 3.1 on 2022-06-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_billcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billcode',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
