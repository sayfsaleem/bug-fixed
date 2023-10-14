from django.urls import path 
from . import views


urlpatterns = [
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('create-product/', views.CreateProduct, name='create-product'),
    path('current-user/', views.CurrentUser, name='current')
]


