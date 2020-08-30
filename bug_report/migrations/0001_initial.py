# Generated by Django 3.1 on 2020-08-30 09:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0004_auto_20200830_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bugs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_title', models.CharField(max_length=150)),
                ('bug_description', models.TextField()),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to='Bug_Reports')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projects')),
            ],
        ),
    ]