from django.contrib import admin
from blog.models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):

    """Docstring for PostAdmin. """
    list_display = ('title', 'created_at', 'views')

admin.site.register(Post, PostAdmin)
