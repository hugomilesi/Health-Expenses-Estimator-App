# predictions/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.model_predict, name='model_predict'),
    path('register/', views.user_signup, name='register'),
    path('login/', views.user_login, name="login"),
    path('logout/', views.logout_view, name = "logout")
]
