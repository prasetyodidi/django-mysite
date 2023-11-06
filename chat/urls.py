from django.urls import path

from . import views

app_name = 'chat'
urlpatterns = [
    path("", views.index, name="index"),
    path('publish', views.publish_message, name='publish'),
]
