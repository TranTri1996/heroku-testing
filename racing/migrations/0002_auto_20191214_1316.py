# Generated by Django 2.0.5 on 2019-12-14 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessory',
            name='owner_id',
        ),
        migrations.RemoveField(
            model_name='accessory',
            name='price',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='like',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author_id',
        ),
        migrations.AddField(
            model_name='accessory',
            name='biker_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='accessory',
            name='market_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='accessory',
            name='status',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accessory',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='comment',
            name='accessory_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='comment',
            name='biker_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_parent_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='like',
            name='accessory_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='like',
            name='biker_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='post',
            name='biker_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='like',
            name='comment_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='like',
            name='post_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='post_id',
            field=models.IntegerField(default=-1),
        ),
    ]
