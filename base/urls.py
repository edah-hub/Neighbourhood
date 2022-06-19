from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='loginPage'),
    path('register/', views.registerPage, name='registerPage'),
    path('logout/', views.logoutUser, name='logout'),
    path('neighbour/', views.neighbour, name='neighbour'),
    path('accountSettings/', views.accountSettings, name='accountSettings'),
    path('post/', views.post, name='post'),
    path('business/', views.business, name='business'),
    path('searchResults/', views.searchResults, name='searchResults'),

]