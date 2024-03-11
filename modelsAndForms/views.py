from django.shortcuts import render

# Create your views here.
#  Главная с 5 случайными рецептами кратко
# * Страница с одним подробным рецептом
# * Страницы регистрации, авторизации и выхода пользователя
# * Страница добавления/редактирования рецепта
# * *другие шаблоны на ваш выбор


def index(request):
    return render(request, "modelsAndForms/index.html")