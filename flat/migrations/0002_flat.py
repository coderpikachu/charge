# Generated by Django 3.0.5 on 2020-05-08 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fId', models.IntegerField()),
                ('layers', models.IntegerField()),
                ('roomNum', models.IntegerField()),
                ('openTime', models.TimeField()),
            ],
            options={
                'db_table': 'flat',
            },
        ),
    ]