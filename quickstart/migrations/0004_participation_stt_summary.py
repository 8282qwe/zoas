# Generated by Django 3.2.8 on 2021-11-04 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('class_id', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'participation_file',
            },
        ),
        migrations.CreateModel(
            name='Stt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(max_length=60)),
                ('stt_file', models.CharField(max_length=100000000)),
            ],
            options={
                'db_table': 'stt_file',
            },
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(max_length=60)),
                ('summary_file', models.CharField(max_length=100000000)),
            ],
            options={
                'db_table': 'summary_file',
            },
        ),
    ]
