from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("resume/", views.resume, name="resume"),
    path("chat-api/", views.chat_api, name="chat_api"),  # FIXED
]
