from . import views
from django.urls import path


urlpatterns = [

    path('',views.demo,name='demo'),
    path('new/', views.new,name='new'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('form', views.form, name='form'),

]