from django.urls import path
from . import views
import store
from store.views import product_list

app_name = 'category'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('<slug:slug>/', store.views.product_list, name='item_list'),
]
