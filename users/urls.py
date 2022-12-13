from django.urls import path
from . import views

urlpatterns = [
   path('users/', views.UserView.as_view()),
   path('users/login/', views.UserLogin.as_view()),
   path('users/<user_id>/', views.UserDetailView.as_view())
]