# Generated by Django 3.0.7 on 2020-07-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200709_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user_id',
        ),
        migrations.AddField(
            model_name='account',
            name='user_email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='birthdate',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='is_social_user',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
