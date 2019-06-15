# Generated by Django 2.1.8 on 2019-06-14 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0004_auto_20190614_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('Small Business', 'sb'), ('Enterprise', 'ent'), ('Professional', 'pro')], max_length=30),
        ),
    ]
