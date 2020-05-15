# Generated by Django 3.0.5 on 2020-05-14 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('flat', '0001_initial'),
        ('dormitory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.User')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=2)),
                ('nation', models.CharField(max_length=100)),
                ('specialty', models.CharField(max_length=100)),
                ('classId', models.IntegerField()),
                ('telephone', models.CharField(max_length=100)),
                ('dormitoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dormitory.Dormitory')),
                ('flatId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flat.Flat')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
