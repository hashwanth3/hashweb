# Generated by Django 3.1.1 on 2020-09-25 12:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20200925_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='created_by',
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweeted_by',
            field=models.TextField(default=datetime.datetime(2020, 9, 25, 12, 39, 1, 270146, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 12, 39, 1, 269998, tzinfo=utc)),
        ),
    ]
