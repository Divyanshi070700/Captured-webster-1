# Generated by Django 3.1.2 on 2020-10-16 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AskMe', '0003_detail_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='contextUrl',
        ),
        migrations.RemoveField(
            model_name='question',
            name='contextUrl',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
        migrations.AddField(
            model_name='answer',
            name='answeredBy',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='question',
            name='postedBy',
            field=models.CharField(default='', max_length=50),
        ),
    ]
