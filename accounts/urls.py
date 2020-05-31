from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('signup/', views.registerpage, name='signup'),
]
