# Generated by Django 3.0.7 on 2020-07-03 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200703_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]