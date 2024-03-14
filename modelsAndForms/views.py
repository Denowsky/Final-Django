from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Recipe, Category, User
from random import randint
from .forms import RecipeForm, UserForm, UserLoginForm

# Create your views here.
#  Главная с 5 случайными рецептами кратко
# * Страница с одним подробным рецептом
# * Страницы регистрации, авторизации и выхода пользователя
# * Страница добавления/редактирования рецепта
# * *другие шаблоны на ваш выбор


def append_sidebar(user={'name': 'Гость'}):
    categories = Category.objects.all()
    recipes = Recipe.objects.all()
    result = []
    random_index = randint(0, len(recipes)-1)
    for _ in range(5):
        result.append(recipes[random_index])
        if random_index == 0:
            random_index = len(recipes)
        random_index-=1
    context = {
        'categories': categories,
        'recipes': result,
        'user': user
    }
    return context


def index(request):
    context = append_sidebar()
    return render(request, "modelsAndForms/index.html", context)


def recipe_edit_form(request, pk):
    try:
        recipe = get_object_or_404(Recipe, pk=pk)
    except Exception:
        return HttpResponse("")
    form = RecipeForm(instance=recipe)
    return render(request, 'modelsAndForms/edit.html', {'form': form, 'recipe_id': pk})


def recipe_form(request):
    form = RecipeForm()
    return render(request, 'modelsAndForms/edit.html', {'form': form})


def recipe_save_edited(request, pk=None):
    if request.method == 'POST':
        if pk == None:
            recipe = Recipe
        else:
            recipe = get_object_or_404(Recipe, pk=pk)
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe.name = form.cleaned_data['name']
            recipe.description = form.cleaned_data['description']
            recipe.steps = form.cleaned_data['steps']
            recipe.time = form.cleaned_data['time']
            recipe.image = form.cleaned_data['image']
            recipe.author = form.cleaned_data['author']
            recipe.category = form.cleaned_data['category']
            recipe.save()
            for data in form.cleaned_data['ingredient']:
                recipe.ingredient.add(data)
            return render(request, 'modelsAndForms/success.html', {'recipe.name': recipe.name})


def recipe_save(request):
    if request.method == 'POST':
        recipe = Recipe()
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe.name = form.cleaned_data['name']
            recipe.description = form.cleaned_data['description']
            recipe.steps = form.cleaned_data['steps']
            recipe.time = form.cleaned_data['time']
            recipe.image = form.cleaned_data['image']
            recipe.author = form.cleaned_data['author']
            recipe.category = form.cleaned_data['category']
            recipe.save()
            for data in form.cleaned_data['ingredient']:
                recipe.ingredient.add(data)
            return render(request, 'modelsAndForms/success.html', {'recipe.name': recipe.name})

def user_form(request):
    form = UserForm()
    return render(request, 'modelsAndForms/register.html', {'form': form})


def save_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        user = User()
        if form.is_valid():
            user.name = form.cleaned_data['name']
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password']
            if not User.objects.filter(email=user.email):
                # return HttpResponse("good")
                user.save()
                context = append_sidebar(user)
                return render(request, "modelsAndForms/index.html", context)
            else:
                return HttpResponse('Юзер с таким email уже зарегестрирован')



def look_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).first()
    return render(request, 'modelsAndForms/recipe.html', {'recipe': recipe})


def login_form(request):
    form = UserLoginForm()
    return render(request, 'modelsAndForms/login.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(email=email).first()
            if user and password == user.password:
                context = append_sidebar(user)
                return render(request, "modelsAndForms/index.html", context)
            else:
                return HttpResponse("Произошла ошибка при входе")
        else:
            return HttpResponse("Произошла ошибка в форме")

def look_category(request, pk):
    category = Category.objects.filter(pk=pk).first()
    recipes = Recipe.objects.filter(category=category)
    context = {
        'recipes': recipes,
        'category': category
    }
    return render(request, 'modelsAndForms/recipes_by.html', context)
