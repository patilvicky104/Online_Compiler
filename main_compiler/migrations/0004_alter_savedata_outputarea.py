# Generated by Django 3.2.2 on 2021-05-30 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_compiler', '0003_auto_20210530_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedata',
            name='outputarea',
            field=models.TextField(null=True),
        ),
    ]