# Generated by Django 3.1.1 on 2020-10-21 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AskMe', '0008_auto_20201021_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ansText',
            field=models.TextField(),
        ),
    ]