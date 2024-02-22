from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
urlpatterns = [
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('me/', UserInfoView.as_view(), name='user_info'),
    path('out/', CustomLogoutView.as_view(), name='logout'),
    path('tokens/', ActiveSessionsView.as_view(), name='tokens'),
    path('out_all/', DeleteAllSession.as_view(), name='logout-all-tokens'),
]