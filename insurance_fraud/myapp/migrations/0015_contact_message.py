# Generated by Django 4.2.3 on 2023-10-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_blog_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
