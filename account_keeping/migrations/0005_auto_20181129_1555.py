# Generated by Django 2.1.3 on 2018-11-29 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_keeping', '0004_auto_20181127_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_number',
            field=models.CharField(default=None, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='routing_number',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
