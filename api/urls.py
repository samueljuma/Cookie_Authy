from django.urls import path, include
from api.views import auth_views, glossary_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'glossary', glossary_views.GlossaryViewSet, basename='glossary')

urlpatterns = [
    path('auth/login', auth_views.LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]