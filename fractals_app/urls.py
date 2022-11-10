from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from fractals_app import views

router = DefaultRouter()
router.register(r"fractals", views.FractalViewSet, basename="fractal")
router.register(r"users", views.UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
]
