# Generated by Django 5.0.6 on 2024-06-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_posts', '0002_remove_blogpost_facebook_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='listing_type',
            field=models.CharField(choices=[('draft', 'draft'), ('public', 'public')], default='draft', max_length=100),
        ),
    ]
