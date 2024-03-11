from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reg', views.user_form, name='register'),
    path('recipe/<int:pk>', views.look_recipe, name='recipe'),
    path('reg/save', views.save_user, name='user'),
]

