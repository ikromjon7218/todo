from rest_framework.views import exception_handler
from django.urls import path, include
from asosiy.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Todo API",
      default_version='v1',
      description="Simple todo API that works with get, post, put, patch, delete methods.   ",
      contact=openapi.Contact("Ikromjon Ibrohimov, <ikromjon7218@gmail.com>"),
     ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
router = DefaultRouter()
router.register('plan', PlanViewSet)


urlpatterns = [
    path('', schema_view.with_ui("swagger", cache_timeout=0)),
    path('', include(router.urls)),
]
