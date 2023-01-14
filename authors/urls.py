from authors import views
from django.urls import include, path

app_name = 'authors'

urlpatterns = [
    path('registro/' ,views.registro, name="register"),
    path('registro/criar/' ,views.criar, name="create"),
]