# Generated by Django 4.2.3 on 2023-10-08 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_cart_id_alter_cart_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_session',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
