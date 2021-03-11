# Generated by Django 3.1.4 on 2021-02-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=50)),
                ('prod_id', models.CharField(max_length=100)),
                ('prod_name', models.CharField(max_length=200)),
                ('prod_price', models.CharField(max_length=50)),
            ],
        ),
    ]
