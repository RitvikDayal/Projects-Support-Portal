# Generated by Django 3.1 on 2020-08-30 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200830_1505'),
        ('bug_report', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bugs',
            new_name='Bug',
        ),
    ]