# Generated by Django 3.0.7 on 2020-07-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(),
        ),
    ]
