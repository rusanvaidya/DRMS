# Generated by Django 3.1 on 2022-02-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users_info',
            fields=[
                ('id', models.IntegerField(max_length=60, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
    ]
