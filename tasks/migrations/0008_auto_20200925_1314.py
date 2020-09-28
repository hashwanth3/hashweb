# Generated by Django 3.1.1 on 2020-09-25 13:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0007_auto_20200925_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 13, 14, 22, 876524, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweeted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]