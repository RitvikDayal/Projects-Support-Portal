# Generated by Django 3.1 on 2020-09-03 05:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_title', models.CharField(max_length=150)),
                ('bug_description', models.TextField()),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to='Bug_Reports')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
