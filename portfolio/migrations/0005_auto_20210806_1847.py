# Generated by Django 3.2.5 on 2021-08-06 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_blog_fullbloglink'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.AddField(
            model_name='project',
            name='tools',
            field=models.CharField(default=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='writeUp',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
