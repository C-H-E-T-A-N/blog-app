from django.contrib import admin
from blog.models import BlogObj,Contact
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    class Media():
        css = {
            "all":("css/main.css",)
        }
        js = ("js/tiny.js",)
admin.site.register(BlogObj, BlogAdmin)
admin.site.register(Contact)