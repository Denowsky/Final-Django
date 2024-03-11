from django.contrib import admin
from .models import Recipe, Category, User

# Register your models here.


@admin.register(User)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password']
    fieldsets = [
        (
            'Регистрация',
            {
                'classes': ['wide'],
                'fields': ['name', 'email', 'password']
            }
        ),
    ]


@admin.register(Recipe)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'description',
                    'steps',
                    'time',
                    'image',
                    'author',
                    'ingredient',
                    'category'
                    ]
    list_filter = ['category']
    search_fields = ['description']
    search_help_text = 'Поиск по описанию'
    readonly_fields = ['author']
    fieldsets = [
        (
            'Основная информация',
            {
                'classes': ['wide'],
                'fields': ['name', 'category', 'author']
            }
        ),
        (
            'Дополнительная информация',
            {
                'classes': ['collapse'],
                'fields': ['description', 'image']
            }
        ),
        (
            'Ингредиенты и время приготовления',
            {
                'fields': ['ingredient', 'time']
            }
        ),
    ]


@admin.register(Category)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['total_price', 'date_ordered']
    fieldsets = [
        (
            'Клиент',
            {
                'fields': ['client']
            }
        ),
        (
            'Продукт',
            {
                'fields': ['products']
            }
        ),
        (
            'Сумма и дата заказа',
            {
                'fields': ['total_price', 'date_ordered']
            }
        ),
    ]
