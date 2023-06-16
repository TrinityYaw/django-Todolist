from django.urls import path

from .views import *


my_app= 'base'

urlpatterns = [
    path("", TaskList.as_view(), name="index" ),
    path("login/", TaskLogin.as_view(), name="login"),
    path("register/", RegisterTask.as_view(), name = "register"),
    path("logout/", TaskLogout.as_view(), name="logout"),
    path("detail/<int:pk>", TaskDetail.as_view(), name="detail"),
    path("create/", CreateView.as_view(), name= "CreateView"),
    path("update/<int:pk>/", TaskUpdate.as_view(), name= "update"),
    path("delete/<int:pk>/", TaskDelete.as_view(), name= "delete"),
    
]
