from django.contrib import admin
from blog.models import Post, Comment, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)

admin.site.register(Category, CategoryAdmin)