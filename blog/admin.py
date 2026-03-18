from django.contrib import admin
from  .models import Post, Category, Comment
# Register yours models here.


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)


