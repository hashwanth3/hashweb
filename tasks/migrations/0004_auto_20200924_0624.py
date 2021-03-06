# Generated by Django 3.1.1 on 2020-09-24 06:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200924_0449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2020, 9, 24, 6, 24, 42, 734588, tzinfo=utc))),
                ('completed_at', models.DateTimeField(null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PE', 'Pending'), ('CO', 'Completed'), ('DR', 'Dropped')], default='PE', max_length=2)),
                ('tags', models.ManyToManyField(blank=True, null=True, to='tasks.Tag')),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
