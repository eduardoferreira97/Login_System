from django.urls import path

from authors import views

app_name = 'authors'

urlpatterns = [
    path('registro/', views.register_view, name="register"),
    path('registro/criar/', views.register_create, name="register_create"),
    path('login/', views.login_view, name="login"),
    path('login/criar/', views.login_create, name="login_create"),
    path('logout/', views.logout_view, name="logout"),
]
