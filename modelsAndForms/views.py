from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Recipe, Category, User
from random import randint
from .forms import RecipeForm, UserForm

# Create your views here.
#  Главная с 5 случайными рецептами кратко
# * Страница с одним подробным рецептом
# * Страницы регистрации, авторизации и выхода пользователя
# * Страница добавления/редактирования рецепта
# * *другие шаблоны на ваш выбор


def index(request):
    categories = Category.objects.all()
    recipes = Recipe.objects.all()
    result = []
    for _ in range(5):
        result.append(recipes[randint(0, len(recipes)-1)])
    context = {
        'categories': categories,
        'recipes': result
    }
    return render(request, "modelsAndForms/index.html", context)

def recipe_form(request):
    if request.method == 'POST':
        try: 
            pk = request.POST.get("recipe_id")
            recipe = get_object_or_404(Recipe, pk=pk)
        except Exception:
            return HttpResponse("")
        form = RecipeForm(instance=recipe)
        return render(request, 'modelsAndForms/recipe.html', {'form': form, 'recipe_id' : pk})
    
def user_form(request):
        form = UserForm()
        return render(request, 'modelsAndForms/register.html', {'form': form})


def save_user(request, pk):
    if request.method == 'POST':
        form = UserForm(request.POST)
        user = User.objects.get(pk=pk)
        if form.is_valid():
            user.name = form.cleaned_data['name']
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password']
            user.save()

def look_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).first()
    return render(request, 'modelsAndForms/recipe.html', {'recipe' : recipe})