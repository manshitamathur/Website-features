# Generated by Django 3.2.5 on 2021-07-22 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='contents',
            field=models.FileField(upload_to='media/'),
        ),
    ]
