from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import ItemViewSet, RandomNumberView
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/layout/<int:number>/', RandomNumberView.as_view(), name='layout'),
    path('', TemplateView.as_view(template_name='index.html')),
]
