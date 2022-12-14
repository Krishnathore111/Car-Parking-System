# Generated by Django 4.1.2 on 2022-11-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=300)),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
