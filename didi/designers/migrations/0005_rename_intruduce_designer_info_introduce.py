# Generated by Django 3.2.4 on 2021-06-29 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designers', '0004_designer_info_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='designer_info',
            old_name='intruduce',
            new_name='introduce',
        ),
    ]
