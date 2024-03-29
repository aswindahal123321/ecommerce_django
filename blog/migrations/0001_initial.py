# Generated by Django 5.0.1 on 2024-02-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('Heading', models.CharField(default='', max_length=500)),
                ('cHeading', models.CharField(default='', max_length=5000)),
                ('subHeading', models.CharField(default='', max_length=500)),
                ('csubheading', models.CharField(default='', max_length=5000)),
                ('category', models.CharField(default='', max_length=50)),
                ('thumbnail', models.ImageField(default='', upload_to='blog/images/')),
                ('date_pub', models.DateField()),
            ],
        ),
    ]
