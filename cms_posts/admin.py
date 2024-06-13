from django.contrib import admin
from .models import BlogPost, BlogPostLike, BlogPostComment, BlogCommentLike
from .models import BlogCommentReply, BlogCommentReplyLike

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(BlogPostLike)
admin.site.register(BlogPostComment)
admin.site.register(BlogCommentLike)
admin.site.register(BlogCommentReply)
admin.site.register(BlogCommentReplyLike)