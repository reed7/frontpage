# Generated by Django 2.0 on 2017-12-26 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0007_auto_20171226_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionanswer',
            name='display_order',
        ),
    ]
