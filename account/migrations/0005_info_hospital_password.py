# Generated by Django 3.1 on 2022-02-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20220215_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='info_hospital',
            name='password',
            field=models.CharField(default='teaching', max_length=50),
        ),
    ]