
from django.contrib import admin
from django.urls import path, include
from spotify import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.register, name='register'),
    path('accounts/',include('users.urls')),
    path('', views.IndexView.as_view(), name='index')
]
