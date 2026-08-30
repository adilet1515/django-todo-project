
from django.urls import path

from .views import index, CreateUser, UserLogin, UserLogout

app_name = "users"

urlpatterns = [
    path("", index, name="index"),
    path("create_user/", CreateUser.as_view(), name="create_user" ),
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", UserLogout.as_view(), name="logout"),

]