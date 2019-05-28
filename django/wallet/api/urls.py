from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("send/", views.send_from, name="from"),  # TODO update data
    path("login/", views.login, name="login")
]
