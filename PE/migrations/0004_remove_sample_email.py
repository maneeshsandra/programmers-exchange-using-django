# Generated by Django 3.0.5 on 2020-05-06 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0003_remove_sample_firstname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='email',
        ),
    ]
