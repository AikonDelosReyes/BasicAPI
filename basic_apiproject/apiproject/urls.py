from django.urls import path
from . import views

app_name = "apiproject"

urlpatterns = [
    path('api/items/', views.get_all_items, name="get_all_items"),
    path('api/items/filter/', views.filter_items, name="filter_items"),
    path('api/items/add/', views.add_item, name="add_item"),
    path('api/items/<int:item_id>/', views.get_item, name="get_item"),
    path('api/items/update/<int:item_id>/', views.update_item, name="update_item"),
    path('api/items/delete/<int:item_id>/', views.delete_item, name="delete_item"),
]