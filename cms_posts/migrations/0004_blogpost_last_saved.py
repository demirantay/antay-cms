# Generated by Django 5.0.6 on 2024-06-14 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_posts', '0003_blogpost_listing_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='last_saved',
            field=models.DateTimeField(auto_now=True),
        ),
    ]