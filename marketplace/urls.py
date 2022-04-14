from django.urls import path
from .views import customers_list
from .views import login

urlpatterns = [
    path('customers/', customers_list, name='customers_url'),
    path('login/', login, name="login"),
]