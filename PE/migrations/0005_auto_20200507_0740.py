# Generated by Django 3.0.5 on 2020-05-07 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0004_remove_sample_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sample',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='rname',
            new_name='firstname',
        ),
    ]
