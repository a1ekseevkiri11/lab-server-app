from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import redirect
from django.views import View
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.shortcuts import render
from django.core.exceptions import ValidationError
from .forms import CustomUserCreationForm, CustomUserCreationForm
from .models import CustomUser

class CustomLoginView(LoginView):
    template_name = 'lab2/login.html'

    def get_success_url(self):
        return reverse_lazy('user_info')
    

class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse_lazy('login')) 


class UserInfoView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'lab2/user_info.html'

    def get_object(self, queryset=None):
        if self.request.user == self.get_user():
            return self.get_user()
        else:
            raise Http404("You don't have permission to view this user's information.")

    def get_user(self):
        return self.request.user



class CustomRegisterView(CreateView, UserPassesTestMixin):
    template_name = 'lab2/register.html' 
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login') 

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    
    def handle_no_permission(self):
        return redirect('user_info') 
    
    def test_func(self):
        return not self.request.user.is_authenticated
    


class ActiveSessionsView(View, LoginRequiredMixin):
    template_name = 'lab2/active_sessions.html'

    def get(self, request, *args, **kwargs):
        active_sessions = self.get_active_sessions()
        return render(request, self.template_name, {'active_sessions': active_sessions})

    def get_active_sessions(self):
        threshold_time = timezone.now() - timezone.timedelta(minutes=2)


        active_sessions = Session.objects.filter(expire_date__gt=threshold_time)

        return active_sessions


class DeleteAllSession(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        self.delete_all_sessions()
        return redirect(reverse_lazy('login'))
    
    def delete_all_sessions(self):
        all_sessions = Session.objects.all()
        for session in all_sessions:
            session.delete()
    
