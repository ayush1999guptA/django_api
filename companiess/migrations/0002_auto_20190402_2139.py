# Generated by Django 2.1.7 on 2019-04-02 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companiess', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='id',
        ),
        migrations.AlterField(
            model_name='stock',
            name='ticker',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
