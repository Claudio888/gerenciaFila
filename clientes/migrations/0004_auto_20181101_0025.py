# Generated by Django 2.1.2 on 2018-11-01 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20181028_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='deficiency_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
