# Generated by Django 5.0.1 on 2024-02-17 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
    ]
