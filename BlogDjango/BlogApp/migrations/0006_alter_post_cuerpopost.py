# Generated by Django 3.2.9 on 2022-01-11 20:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0005_auto_20220110_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cuerpoPost',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]