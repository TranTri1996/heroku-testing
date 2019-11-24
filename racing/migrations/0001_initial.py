# Generated by Django 2.2.7 on 2019-11-24 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biker',
            fields=[
                ('id', models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100, null=True)),
                ('address_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)),
                ('biker_id', models.CharField(max_length=24)),
                ('status', models.TextField(null=True)),
            ],
        ),
    ]
