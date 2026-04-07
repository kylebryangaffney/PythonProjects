from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'), ## URL path for home page
    path('create/', views.create_account, name='create'), ## url to create new accounts
    path('<int:pk>/balance/', views.balance, name='balance'), ## url to view balance of a particular primary key of an account
    path('transaction/', views.transaction, name='transaction') # url to enter a new transaction
]

