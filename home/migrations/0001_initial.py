# Generated by Django 3.1 on 2022-01-20 12:12

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('phone', models.IntegerField(blank=True)),
                ('message', models.TextField(blank=True, max_length=255)),
                ('ip', models.CharField(blank=True, max_length=100)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=50)),
                ('address', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/logo/')),
                ('icontext', models.ImageField(blank=True, null=True, upload_to='images/logo/')),
                ('iconblue', models.ImageField(blank=True, null=True, upload_to='images/logo/')),
                ('iconwhite', models.ImageField(blank=True, null=True, upload_to='images/logo/')),
                ('iconfav', models.ImageField(blank=True, null=True, upload_to='images/logo/')),
                ('facebook', models.CharField(blank=True, max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=50)),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('youtube', models.CharField(blank=True, max_length=50)),
                ('aboutus', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('donate', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('what_we_do', models.TextField(blank=True, null=True)),
                ('our_mission', models.TextField(blank=True, null=True)),
                ('our_vision', models.TextField(blank=True, null=True)),
                ('references', models.TextField(blank=True, null=True)),
                ('privacypolicy', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('tandc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]