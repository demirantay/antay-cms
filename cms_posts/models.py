# Main Imports

# Django Imports
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# My Module Imports
from authentication.models import BasicUserProfile


class BlogPost(models.Model):
    """
    Data: Posts of the Blog
    """
    id = models.AutoField(primary_key=True)
    creation_date = models.DateField(default=timezone.now)
    author = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    title = models.CharField(max_length=1000)
    CATEGORY_TYPES = (
        ('sport', 'sport'),
        ('tech', 'tech'),
        ('fishing', 'fishing'),
    )
    category = models.CharField(max_length=100, choices=CATEGORY_TYPES)
    content = models.TextField()

    def __str__(self):
        return "Title: " + str(self.title)


class BlogPostLike(models.Model):
    """
    Data: Blog Posts likes made by other users
    """
    id = models.AutoField(primary_key=True)
    creation_date = models.DateField(default=timezone.now)
    liked_post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    like_owner = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return "Post: " + str(self.liked_post)


class BlogPostComment(models.Model):
    """
    Data: Blog posts comments made by other users
    """
    id = models.AutoField(primary_key=True)
    creation_date = models.DateField(default=timezone.now)
    comment_post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    comment_owner = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    content = models.TextField()

    def __str__(self):
        return "Blog Comment: " + str(self.comment_owner) + "/" \
                + str(self.comment_post)


class BlogCommentLike(models.Model):
    """
    Data: Blog Comment Like made by other users
    """
    id = models.AutoField(primary_key=True)
    creation_date = models.DateField(default=timezone.now)
    liked_comment = models.ForeignKey(
        BlogPostComment,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    like_owner = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return "Comment: " + str(self.liked_comment) + "| owner: " + \
                str(self.like_owner)


class BlogCommentReply(models.Model):
    """
    Data: Blog Comment reply made by other users
    """
    id = models.AutoField(primary_key=True)
    creation_date = models.DateField(default=timezone.now)
    comment = models.ForeignKey(
        BlogPostComment,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    reply_owner = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    content = models.TextField()

    def __str__(self):
        return "Comment" + str(self.comment) + "/ reply: " + str(self.content)



class BlogCommentReplyLike(models.Model):
    """
    Blog Comment reply's likes made by other users
    """
    id = models.AutoField(primary_key=True)
    creation_date = models.DateField(default=timezone.now)
    liked_reply = models.ForeignKey(
        BlogPostComment,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    like_owner = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return "Reply:" + str(self.liked_reply) + "/ liker: " + \
                str(self.like_owner)