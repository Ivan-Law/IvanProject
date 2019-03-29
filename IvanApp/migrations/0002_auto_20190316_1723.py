# Generated by Django 2.1.5 on 2019-03-16 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IvanApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myinput',
            name='myticker',
        ),
        migrations.AddField(
            model_name='myinput',
            name='dailypnl',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myinput',
            name='lastprice',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myinput',
            name='lasttradeday',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myinput',
            name='mtdpnl',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myinput',
            name='stockticker',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myinput',
            name='ytdpnl',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
