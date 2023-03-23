from django.urls import path
from Portfolioapp import views

urlpatterns = [
    
    path('', views.Home, name="Home"),
    path('projects/', views.Projects, name="Projects"),

]
