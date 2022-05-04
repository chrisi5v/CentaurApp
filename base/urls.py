from  django.urls import path
from  . import views

urlpatterns =  [
    path('login/', views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('', views.home , name  = "home"),
    
    path('create-checklist/', views.createChecklist, name="create-checklist"),
    path('update-checklist/<str:pk>/', views.updateChecklist, name="update-checklist"),
    path('view-checklist/<str:pk>/', views.viewChecklist, name="view-checklist"),
]
