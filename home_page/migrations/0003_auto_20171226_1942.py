# Generated by Django 2.0 on 2017-12-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_auto_20171226_1937'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QandA',
            new_name='QuestionAnswer',
        ),
        migrations.AlterField(
            model_name='contactmethod',
            name='contact_type',
            field=models.CharField(choices=[('tt', 'Twitter'), ('fb', 'Facebook'), ('em', 'Email'), ('wc', 'WeChat'), ('ma', 'Mailing'), ('gh', 'Github'), ('cp', 'Codepen'), ('lk', 'Linkedin'), ('ce', 'Cellphone'), ('ot', 'Other')], max_length=2, unique=True),
        ),
    ]
