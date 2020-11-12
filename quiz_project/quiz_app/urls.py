from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [
	path('dashboard/', views.dashboard, name='account-dashboard'),
    path('login/', auth_views.LoginView.as_view(
    	template_name='quiz_app/login.html'), name='account-login'),
    path('logout/', auth_views.LogoutView.as_view(
    	template_name='quiz_app/logout.html'), name='account-logout')
]