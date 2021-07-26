from django.conf.urls import url
from django.urls import path
from tabledbt import views

urlpatterns = [
    url(r'^$',views.home,name = 'home'),
    url(r'^table_view',views.table_view,name = 'table_view'),
    #path('home/',views.home, name = 'home'),
    #path('home/table_view/', views.table_view, name = 'table_view')
]