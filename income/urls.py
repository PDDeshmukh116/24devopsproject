

from django.urls import path
from .import views as v
urlpatterns = [
    path("add_income",v.addincome,name='add'),
    path("list",v.income_list,name='list'),
    path("delet/<int:id>",v.delete_income,name='delete'),
    path("income_search",v.income_search,name="income_search"),
    path("edit/<int:id>",v.editIncome,name="edit")
]
