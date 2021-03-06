# Generated by Django 3.2.5 on 2021-08-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('tools', models.TextField()),
                ('fullBlog', models.TextField()),
                ('fullBlogLink', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='portfolio/videos/'),
        ),
    ]
