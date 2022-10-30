from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ItemList, ItemDetail


urlpatterns = [
    path('items/', ItemList.as_view()),
    path('items/<int:pk>/', ItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)