from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet


post_router = DefaultRouter()
post_router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(post_router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/signup/', include('dj_rest_auth.registration.urls')),
]
