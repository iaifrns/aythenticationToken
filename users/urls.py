from django.urls import path
from .views import login_api, register_api, get_user_data, addcolor, getObject, deleteObject, addobject

urlpatterns = [
    path('login/', login_api.as_view()),
    path('users/', get_user_data.as_view()),
    path('register/', register_api.as_view()),
    path('listobject/', getObject.as_view()),
    path('deleteobject/', deleteObject.as_view()),
    path('addobject/', addobject.as_view()),
    path('addcolor/', addcolor.as_view())
]