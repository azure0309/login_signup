# Generated by Django 2.2.7 on 2019-11-20 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191118_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
