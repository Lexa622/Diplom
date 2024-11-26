from django.contrib import admin
from .models import Post


# Админка для модели Category
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_posted', 'author')    # Поля для отображения в списке
    search_fields = ('title', 'content')   # Поля для поиска
