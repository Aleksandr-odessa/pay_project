from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:item_id>/', views.detail, name='detail'),
    path('buy/<int:buy_id>/', views.buy, name ='buy'),
]