# Generated by Django 3.2.5 on 2021-08-06 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_blog_fullbloglink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='fullBlogLink',
        ),
    ]
