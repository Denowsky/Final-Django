from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reg', views.user_form, name='register'),
    path('recipe/<int:pk>', views.look_recipe, name='recipe'),
    path('category/<int:pk>', views.look_category, name='category'),
    path('recipe/edit/<int:pk>', views.recipe_edit_form, name='edit'),
    path('edit/', views.recipe_form, name='edit'),
    path('recipe/edit/save/<int:pk>', views.recipe_save_edited, name='save'),
    path('edit/save/', views.recipe_save, name='save'),
    path('user', views.save_user, name='logged'),
    path('login', views.login_form, name='login'),
    path('main', views.login, name='logged'),
]

