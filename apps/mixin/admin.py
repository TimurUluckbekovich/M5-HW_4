from django.contrib import admin
from .models import Post, Client


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Колонки, отображаемые в списке статей
    list_display = ('id', 'title', 'category', 'views_count', 'is_published', 'created')
    
    # Поля, по которым работает строка поиска
    search_fields = ('title', 'category', 'description')
    
    # Панель фильтров справа
    list_filter = ('is_published', 'category', 'created')
    
    # Редактирование галочки "Опубликовано" прямо из списка
    list_editable = ('is_published',)
    
    # Количество записей на одной странице
    list_per_page = 20


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # Колонки, отображаемые в списке клиентов (напомним: title унаследован как ФИО/Компания)
    list_display = ('id', 'title', 'phone', 'email', 'is_active', 'created')
    
    # Поиск по ФИО, телефону, почте и адресу
    search_fields = ('title', 'phone', 'email', 'address', 'description')
    
    # Фильтрация по статусу (активен/в архиве) и дате
    list_filter = ('is_active', 'created')
    
    # Быстрое переключение статуса клиента
    list_editable = ('is_active',)
    
    list_per_page = 20