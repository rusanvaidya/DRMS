# Generated by Django 3.1 on 2022-02-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_info_hospital_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_hospital',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]