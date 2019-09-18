from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import UserAuthenticationForm, UserPasswordChange, UserPasswordReset, UserSetPassword
from . import views

urlpatterns = [
    # post views
    #path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(authentication_form = UserAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(form_class = UserPasswordChange), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(form_class = UserPasswordReset), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(form_class = UserSetPassword), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit_user_profile/', views.EditUserProfile, name='edit_user_profile'),
]