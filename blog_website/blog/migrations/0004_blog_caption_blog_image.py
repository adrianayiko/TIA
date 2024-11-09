# Generated by Django 5.1.3 on 2024-11-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_author_delete_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='caption',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
    ]
