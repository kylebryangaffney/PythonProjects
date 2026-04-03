
from django.urls import path
from . import views

app_name = 'profiles'


urlpatterns = [
    path('', views.profile_list, name="profile_list"),
    path('<int:pk>/profile_detail/', views.profile_detail, name="profile_details"), 
    path('<int:pk>/profile_delete/', views.profile_delete, name="profile_delete"),
    path('profile_confirmed/', views.profile_confirmed, name="profile_confirmed"),
    path('profile_create/', views.profile_create, name="profile_create"),
]


