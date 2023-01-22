from django.urls import path

from main.views import RegisterUser

urlpatterns = [
    path('', RegisterUser.as_view(), name='register'),
]