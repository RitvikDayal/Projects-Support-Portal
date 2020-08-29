# Generated by Django 3.1 on 2020-08-29 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('project_image', models.ImageField(default='default_project.png', upload_to='project_pics')),
                ('summary', models.CharField(max_length=120)),
                ('date_posted', models.DateTimeField()),
                ('deploy_link', models.URLField(max_length=500)),
                ('tag', models.CharField(default='personal', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
