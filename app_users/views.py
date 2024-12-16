from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import  redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth import get_user_model


from .forms import UserRegistrationForm


User = get_user_model()


class UserLogin(LoginView):
    template_name = 'login.html'
    extra_context = {
        'is_login': True,
    }

    def get_success_url(self):
        return self.request.POST.get('next')


class UserRegistration(CreateView):
    template_name = 'registration.html'
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')


def user_logout(request):
    logout(request)
    return redirect('home')

