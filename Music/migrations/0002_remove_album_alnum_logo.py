# Generated by Django 2.2.2 on 2019-06-14 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='alnum_logo',
        ),
    ]
