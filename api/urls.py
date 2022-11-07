from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ItemList, ItemDetail
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('items/', ItemList.as_view()),
    path('items/<int:pk>/', ItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)