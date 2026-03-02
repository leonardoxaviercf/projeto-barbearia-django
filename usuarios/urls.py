from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='usuarios/password_change_form.html',
        success_url='/usuarios/password_change/done/' 
    ), name='password_change'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='usuarios/password_change_done.html'
    ), name='password_change_done'),
]