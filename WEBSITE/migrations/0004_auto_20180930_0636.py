# Generated by Django 2.1 on 2018-09-30 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBSITE', '0003_auto_20180925_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registertable',
            name='uname',
            field=models.IntegerField(),
        ),
    ]
