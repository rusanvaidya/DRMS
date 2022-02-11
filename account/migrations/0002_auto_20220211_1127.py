# Generated by Django 3.1 on 2022-02-11 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='info_doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('license_no', models.ImageField(upload_to='license')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('field', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='info_hospital',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hospital_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('hospitalpan', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='info_patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('citizen_no', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='info_user',
        ),
    ]