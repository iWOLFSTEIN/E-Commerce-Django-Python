# Generated by Django 5.0.7 on 2024-08-15 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0006_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='9e648236d7154a4aba421c41ea6dabd1', max_length=24, primary_key=True, serialize=False),
        ),
    ]
