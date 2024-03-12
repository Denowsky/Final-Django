from django.contrib import admin
from .models import Recipe, Category, User, Ingredient

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
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
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'image',
                    'author',
                    'category'
                    ]
    list_filter = ['category']
    search_fields = ['description']
    search_help_text = 'Поиск по описанию'
    fieldsets = [
        (
            'Основная информация',
            {
                'classes': ['wide'],
                'fields': ['name', 'category', 'author']
            }
        ),
        (
            'Ингредиенты и время приготовления',
            {
                'fields': ['ingredient', 'time']
            }
        ),
        (
            'Дополнительная информация',
            {
                'classes': ['collapse'],
                'fields': ['description', 'steps', 'image']
            }
        ),
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    fieldsets = [
        (
            'Категории',
            {
                'fields': ['category_name']
            }
        ),
    ]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['ing_name', 'kcal']
    fieldsets = [
        (
            'Продукт',
            {
                'fields': ['ing_name']
            }
        ),
        (
            'Калории',
            {
                'fields': ['kcal']
            }
        ),

    ]
