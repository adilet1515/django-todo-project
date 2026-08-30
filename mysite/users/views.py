from django.contrib.auth.views import LoginView, LogoutView

from .forms import UserCreationForm, User
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.


def index(request):
    return render(request, "todo/index.html")

class CreateUser(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = "registration/user_create_form.html"
    success_url = reverse_lazy('users:login')

class UserLogin(LoginView):
    next_page = reverse_lazy('users:index')


class UserLogout(LogoutView):
    template_name = "registration/logout_form.html"
    next_page = reverse_lazy('users:index')
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
        )

