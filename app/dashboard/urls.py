from django.urls import path
from . import views

urlpatterns=[
    path('user/',views.get_user,name='get_user'),
    path('add_friend/', views.add_friend, name='add_friend'),
]