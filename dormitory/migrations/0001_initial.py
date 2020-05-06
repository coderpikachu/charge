# Generated by Django 3.0.5 on 2020-05-06 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flat', '0001_initial'),
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
                ('flatId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flat.Flat')),
            ],
            options={
                'db_table': 'dormitory',
            },
        ),
    ]