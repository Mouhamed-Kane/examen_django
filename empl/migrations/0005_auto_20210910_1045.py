# Generated by Django 2.2.24 on 2021-09-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empl', '0004_auto_20210910_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=1, max_digits=8),
        ),
    ]
