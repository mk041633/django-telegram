# Generated by Django 3.1.6 on 2023-08-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_auto_20230815_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
