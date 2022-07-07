from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes, name="api-overview"),
    path('get_st_users/', views.getSt_users, name="get_st_users"),
    path('add_st_user/', views.addSt_user, name="add_st_user"),
    path('get_univs/', views.getUnivs, name="get_univs"),
    path('get_degrees/', views.getDegrees, name="get_degrees"),
    # path('login/', views.getTest, name="login"),
    # path('register/', views.getTest, name="register"),
    path('edit/', views.edit, name="edit"),
    path('some_view/', views.some_view, name="some_view"),

    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('test/', views.getTest, name="test"),
]