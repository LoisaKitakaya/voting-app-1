# Generated by Django 4.1.1 on 2022-11-18 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('personal_id', models.CharField(max_length=254)),
                ('department', models.CharField(max_length=254)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Current Employees',
                'ordering': ['-created_date'],
            },
        ),
    ]
