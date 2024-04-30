from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('reg', views.VkRegView.as_view(), name='reg'),
    path('vkApi/<int:pk>/', views.UserProfileView.as_view(), name='vkApi'),
]