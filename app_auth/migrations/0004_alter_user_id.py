# Generated by Django 5.0.7 on 2024-08-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0003_remove_productreview_product_alter_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='05a96d402c0247c6a221a071a987fd3e', max_length=24, primary_key=True, serialize=False),
        ),
    ]
