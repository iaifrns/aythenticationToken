from django.urls import path
from .views import login_api, register_api, get_user_data

urlpatterns = [
    path('login/', login_api.as_view()),
    path('users/', get_user_data.as_view()),
    path('register/', register_api.as_view()),
]