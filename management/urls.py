from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('home/', views.loginHome, name='home'),
    path('profile/', views.profile, name='profile'),
    path('apply-for-leave/', views.apply, name='apply'),
    path('approval-list/', views.approval, name='approve'),
    path('approval-list/<str:pk>/approved/', views.approve, name='approved'),
    path('approval-list/<str:pk>/declined/', views.decline, name='declined'),
]
