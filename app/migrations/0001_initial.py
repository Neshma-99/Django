# Generated by Django 3.2.2 on 2021-06-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('emp_code', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('position', models.CharField(max_length=10)),
            ],
        ),
    ]