# Generated by Django 2.0.5 on 2019-12-14 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='', null=True)),
                ('price', models.DecimalField(decimal_places=3, default=0.0, max_digits=20)),
                ('like_number', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'accessory_tab',
            },
        ),
        migrations.CreateModel(
            name='Biker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('email', models.CharField(max_length=100)),
                ('hash_password', models.CharField(default='', max_length=100)),
                ('password_salt', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=1)),
                ('main_address_id', models.IntegerField(null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.SmallIntegerField(default=0)),
                ('job', models.CharField(default='', max_length=50)),
                ('facebook', models.CharField(default='', max_length=100)),
                ('like_number', models.IntegerField(default=0)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'db_table': 'biker_tab',
            },
        ),
        migrations.CreateModel(
            name='BikerAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=255)),
                ('contact_name', models.CharField(default='', max_length=255)),
                ('contact_phone', models.CharField(default='', max_length=15)),
                ('biker_id', models.BigIntegerField(db_index=True)),
                ('district_id', models.BigIntegerField()),
                ('province_id', models.BigIntegerField()),
                ('ward_id', models.BigIntegerField()),
                ('longitude', models.DecimalField(decimal_places=6, default=0, max_digits=20)),
                ('latitude', models.DecimalField(decimal_places=6, default=0, max_digits=20)),
                ('type', models.SmallIntegerField(default=0)),
                ('deleted', models.SmallIntegerField(default=0)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'biker_address_tab',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
                ('author_id', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='racing.Biker')),
            ],
            options={
                'db_table': 'comment_tab',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
                ('author_id', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='racing.Biker')),
                ('comment_id', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='racing.Comment')),
            ],
            options={
                'db_table': 'like_tab',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_number', models.IntegerField(default=0)),
                ('share_number', models.IntegerField(default=0)),
                ('view_number', models.IntegerField(default=0)),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='', null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
                ('author_id', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='racing.Biker')),
            ],
            options={
                'db_table': 'post_tab',
            },
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('url', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'post_image_tab',
            },
        ),
        migrations.AddField(
            model_name='like',
            name='post_id',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='racing.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='racing.Post'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='owner_id',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='racing.Biker'),
        ),
    ]
