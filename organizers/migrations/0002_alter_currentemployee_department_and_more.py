# Generated by Django 4.1.1 on 2022-11-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentemployee',
            name='department',
            field=models.CharField(choices=[('Procurement and Logistics', 'dept of procurement and logistics'), ('Economics', 'dept of economics'), ('Accounting and Finance', 'dept of accounting and finance'), ('Business Administration', 'dept of business administration'), ('Engineering', 'dept of engineering'), ('Construction and Textile', 'dept of construction and textile'), ('Entrepreneurship and Technology', 'dept of entrepreneurship and technology'), ('Leadership and Management', 'dept of leadership and management')], max_length=254),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='department',
            field=models.CharField(choices=[('Procurement and Logistics', 'dept of procurement and logistics'), ('Economics', 'dept of economics'), ('Accounting and Finance', 'dept of accounting and finance'), ('Business Administration', 'dept of business administration'), ('Engineering', 'dept of engineering'), ('Construction and Textile', 'dept of construction and textile'), ('Entrepreneurship and Technology', 'dept of entrepreneurship and technology'), ('Leadership and Management', 'dept of leadership and management')], max_length=254),
        ),
    ]
