# Generated by Django 3.0.7 on 2020-10-30 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_dept_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='')),
                ('author', models.CharField(default='anonymous', max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('describe', models.TextField(default='CRUD Django tutorials')),
            ],
        ),
    ]
