# Generated by Django 3.0.5 on 2020-05-06 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dormitory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dId', models.IntegerField()),
                ('peopleNum', models.IntegerField()),
                ('accommodationCharge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('telephone', models.IntegerField()),
                ('flatId', models.IntegerField()),
            ],
            options={
                'db_table': 'dormitory',
            },
        ),
    ]
