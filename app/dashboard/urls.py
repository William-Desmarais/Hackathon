from django.urls import path
from . import views

urlpatterns=[
    path('user/',views.get_user,name='get_user'),
    path('add_friend/', views.add_friend, name='add_friend'),
    path('del_friend/', views.del_friend, name='del_friend'),
    path('add_points/', views.add_points, name='add_points'),
    path('clear_points/', views.clear_points, name='clear_points'),  
    path('set_goal/', views.set_goal, name='set_goal'), 
    path('about_us/', views.about, name='about'), 
]