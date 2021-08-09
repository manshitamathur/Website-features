# Generated by Django 3.2.5 on 2021-07-22 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribeModel',
            fields=[
                ('sys_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=200, unique=True)),
                ('status', models.CharField(blank=True, max_length=64)),
                ('created_date', models.DateTimeField(blank=True)),
                ('updated_date', models.DateTimeField(blank=True)),
            ],
            options={
                'db_table': 'myapp_subscribe',
            },
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(help_text='Write here your message!'),
        ),
    ]
