from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from app.views import PlayerViewSet, CardViewSet, GameViewSet, RandomNumberView, UserRegistrationView, UserViewSet
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'cards', CardViewSet)
router.register(r'games', GameViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/old/auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('api/old/auth/register/', UserRegistrationView.as_view(), name='register_user'),
    path('api/shuffledCards/<int:number>/', RandomNumberView.as_view(), name='layout'),
    path('', TemplateView.as_view(template_name='index.html')),
]
