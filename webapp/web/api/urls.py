from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="api-overview"),
    path('get_st_users/', views.getSt_users, name="get_st_users"),
    path('add_st_user/', views.addSt_user, name="add_st_user"),
    path('get_univs/', views.getUnivs, name="get_univs"),
    path('get_degrees/', views.getDegrees, name="get_degrees"),

    path('test/', views.getTest, name="test"),
]