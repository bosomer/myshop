from django.urls import path
from app5 import views

urlpatterns = [
    path('upload_file/', views.upload_file),
    path('userinfo_form/', views.userinfo_form),
]
