# Generated by Django 3.0 on 2021-08-10 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='name',
        ),
    ]
