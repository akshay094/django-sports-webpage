# Generated by Django 3.0 on 2021-08-09 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210809_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('userid', models.IntegerField()),
                ('playerid', models.IntegerField()),
            ],
        ),
    ]
