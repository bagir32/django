# Generated by Django 2.2.16 on 2020-11-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20201122_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='student',
        ),
        migrations.AddField(
            model_name='book',
            name='student',
            field=models.ManyToManyField(default='1', related_name='Book', to='student.Student'),
        ),
    ]
