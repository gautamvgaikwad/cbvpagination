# Generated by Django 3.2.4 on 2021-12-15 11:54

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
                ('ename', models.CharField(max_length=50)),
                ('esal', models.FloatField()),
                ('edept', models.CharField(max_length=50)),
            ],
        ),
    ]
