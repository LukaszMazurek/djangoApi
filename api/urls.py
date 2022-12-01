from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ImageList, ImageDetail, GalleryList, GalleryDetail, UserList, PictureList, HomeSite
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('pictures/', HomeSite.as_view()),
    path('images/', ImageList.as_view()),
    path('images/<int:pk>/', ImageDetail.as_view()),
    path('gallery/', GalleryList.as_view()),
    path('gallery/<int:pk>', GalleryDetail.as_view()),
    path('user/', UserList.as_view()),
    path('pictures/pictureList', PictureList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
