# Generated by Django 3.1 on 2020-08-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='detail',
            field=models.TextField(default='This is the place where more details about the project go.'),
            preserve_default=False,
        ),
    ]
