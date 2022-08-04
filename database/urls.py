from django.contrib import admin
from django.urls import path
from .views import (
    ListView, ListUpdate, ListDel
)

urlpatterns = [
    path('list/', ListView.as_view(), name='create'),
    path('update/', ListUpdate.as_view(), name='update'),
    path('delete/', ListDel.as_view(), name='delete'),
]