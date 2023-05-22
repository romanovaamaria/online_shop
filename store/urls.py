from django.urls import path
from . import views

app_name = 'store'

urlpatterns= [
    path('<int:id>/<slug:slug>/', views.item_detail, name='item_detail')
]