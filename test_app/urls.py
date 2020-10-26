from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import path

from .views import redir, test_list, QuizView,\
    log_out, RegistrationView, VerificationView, LoginView

urlpatterns = [
    path('', redir),
    path('test/', test_list),
    path('test/solve/<id>', login_required(QuizView.as_view())),
    path('authentication/register', RegistrationView.as_view(), name="register"),
    path('authentication/login', LoginView.as_view(), name="login"),
    path('authentication/logout', log_out, name="logout"),
    path('authentication/activate/<uidb64>/<token>',
         VerificationView.as_view(), name='activate'),
]

