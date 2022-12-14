from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('NAmerica/', auth_views.LoginView.as_view(template_name='common/NAmerica.html'), name='NAmerica'),
    path('SAmerica/', auth_views.LoginView.as_view(template_name='common/SAmerica.html'), name='SAmerica'),
    path('Asia/', auth_views.LoginView.as_view(template_name='common/Asia.html'), name='Asia'),
    path('Africa/', auth_views.LoginView.as_view(template_name='common/Africa.html'), name='Africa'),
    path('Europe/', auth_views.LoginView.as_view(template_name='common/Europe.html'), name='Europe'),
    path('Oceania/', auth_views.LoginView.as_view(template_name='common/Oceania.html'), name='Oceania'),
    path('FAQ/', auth_views.LoginView.as_view(template_name='common/FAQ.html'), name='FAQ'),
]