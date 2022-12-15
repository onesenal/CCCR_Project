from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('NAmerica/', views.getContinental, name="NAmerica"),
    path('SAmerica/', views.getContinental, name='SAmerica'),
    path('Asia/', views.getContinental, name='Asia'),
    path('Africa/', views.getContinental, name='Africa'),
    path('Europe/', views.getContinental, name='Europe'),
    path('Oceania/', views.getContinental, name='Oceania'),
    path('FAQ/', auth_views.LoginView.as_view(template_name='common/FAQ.html'), name='FAQ')
]