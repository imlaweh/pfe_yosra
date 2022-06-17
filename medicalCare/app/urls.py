from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
        path("", views.index),
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path("admin/", views.admin),
        path("add_eias/", views.add_eias),
        path('admin/get_data/<str:id>/', views.get_data),
        
]
