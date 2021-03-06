# Generated by Django 3.1.2 on 2020-10-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AskMe', '0005_auto_20201017_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='answered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]
