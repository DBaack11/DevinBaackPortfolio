# Generated by Django 3.2.4 on 2021-08-07 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_project_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='video',
            field=models.FileField(upload_to='portfolio/videos'),
        ),
    ]
