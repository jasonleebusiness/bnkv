# Generated by Django 3.1 on 2022-05-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_setting_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swift_codes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swift_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tax_codes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_code', models.CharField(max_length=20)),
            ],
        ),
    ]