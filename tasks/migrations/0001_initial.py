# Generated by Django 3.1.1 on 2020-09-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('status', models.CharField(choices=[('PE', 'Pending'), ('CO', 'Completed'), ('DR', 'Dropped')], default='PE', max_length=2)),
                ('tags', models.ManyToManyField(to='tasks.Tag')),
            ],
        ),
    ]
