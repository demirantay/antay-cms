# Generated by Django 5.0.6 on 2024-06-13 10:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=1000)),
                ('category', models.CharField(choices=[('sport', 'sport'), ('tech', 'tech'), ('fishing', 'fishing')], max_length=100)),
                ('content', models.TextField()),
                ('twitter_link', models.CharField(max_length=100)),
                ('facebook_link', models.CharField(max_length=100)),
                ('linkedin_link', models.CharField(max_length=100)),
                ('normal_link', models.CharField(max_length=100)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.basicuserprofile')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPostComment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('comment_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.basicuserprofile')),
                ('comment_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms_posts.blogpost')),
            ],
        ),
        migrations.CreateModel(
            name='BlogCommentReplyLike',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('like_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.basicuserprofile')),
                ('liked_reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms_posts.blogpostcomment')),
            ],
        ),
        migrations.CreateModel(
            name='BlogCommentReply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('reply_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.basicuserprofile')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms_posts.blogpostcomment')),
            ],
        ),
        migrations.CreateModel(
            name='BlogCommentLike',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('like_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.basicuserprofile')),
                ('liked_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms_posts.blogpostcomment')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPostLike',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('like_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.basicuserprofile')),
                ('liked_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms_posts.blogpost')),
            ],
        ),
    ]
