from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("new-key/", views.new_key, name="new_key"),
    path("transaction/", views.transaction, name="transaction"),
    path("block/add", views.save_transaction, name="save_transaction"),
    path("transaction/payment", views.send_payment, name="send_payment"),
    path("transaction/send", views.send_transaction, name="send_transaction")
]
