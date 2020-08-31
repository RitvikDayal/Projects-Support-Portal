# Generated by Django 3.1 on 2020-08-31 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200830_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.CharField(max_length=100),
        ),
    ]
