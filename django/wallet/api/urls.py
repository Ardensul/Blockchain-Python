from django.urls import path

from . import views

urlpatterns = [
    path("", views.transaction, name='transaction'),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("transaction/", views.transaction, name="transaction")
]
