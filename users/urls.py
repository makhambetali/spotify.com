from django.contrib import admin
from django.urls import path
from users import views
from django.contrib.auth.views import logout_then_login
app_name = 'users'
urlpatterns = [
    path('registerPage/', views.register_request, name='register'),
    path('login/', views.CustomLoginView.as_view(template_name='users/login.html',extra_context={'next': '/'}), name='login'),
    path('logout/', logout_then_login, name='logout'),
]
