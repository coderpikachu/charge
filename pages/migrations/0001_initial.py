# Generated by Django 3.0.5 on 2020-05-08 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uId', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'pages',
            },
        ),
    ]
