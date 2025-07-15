from django.urls import path, include
from api.views import auth_views

urlpatterns = [
    path('auth/login', auth_views.LoginView.as_view(), name='login'),
]