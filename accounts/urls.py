from django.urls import path
from accounts import views
urlpatterns = [
    path('register/',views.register),
    path('login/',views.login_view),
    path('home/',views.register),
  
]