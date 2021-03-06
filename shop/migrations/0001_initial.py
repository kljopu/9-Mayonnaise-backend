# Generated by Django 3.0.7 on 2020-07-14 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=8)),
            ],
            options={
                'db_table': 'shops',
            },
        ),
    ]
