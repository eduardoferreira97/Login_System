from django.urls import path

from authors import views

app_name = 'authors'

urlpatterns = [
    path('registro/', views.registro, name="register"),
    path('registro/criar/', views.criar, name="create"),
]
