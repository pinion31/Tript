from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'tript'

urlpatterns = [
    url(r'^$', views.LandingView.as_view(), name='landing'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='tript/logout.html'), name='logout'),
    url(r'^login/', views.LoginUserView.as_view(), name='login'),
    url(r'^sign_up/', views.SignUpView.as_view(), name='sign_up'),
    url(r'^dashboard/', views.DashboardView.as_view(), name='dashboard')
]