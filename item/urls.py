from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ItemListView.as_view(), name='item_list'),
    path('detail/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('create/', views.ItemCreateView.as_view(), name='item_create'),
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='item_update'),
    path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='item_delete'),
]
