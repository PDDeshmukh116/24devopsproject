from django.contrib import admin
from django.urls import path
from .import views as v
urlpatterns = [
    path("add_expense",v.addexpense,name='add'),
    path("list",v.expense_list,name='list'),
    path("delete/<int:id>",v.delete_expense,name='delete'),
    path("ext/<str:ext>",v.sort_byexpense_type,name='ext'),
]
