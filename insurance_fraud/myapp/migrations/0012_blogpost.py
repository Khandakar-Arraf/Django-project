# Generated by Django 4.2.3 on 2023-10-13 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100, null=True)),
                ('blog_title', models.CharField(max_length=200, null=True)),
                ('user_image', models.ImageField(default=None, null=True, upload_to='uploads/blogs')),
                ('date', models.DateTimeField(null=True)),
                ('writing', models.TextField(null=True)),
            ],
        ),
    ]