# Generated by Django 4.0 on 2021-12-15 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_post_titulotag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tituloTag',
            new_name='titulo_tag',
        ),
    ]
