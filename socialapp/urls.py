from django.urls import re_path
from django.contrib.auth import views as auth_view
from socialapp import views

app_name = 'socialapp'

urlpatterns = [
    re_path(r'^login/$',
    auth_view.LoginView.as_view(template_name='socialapp/login.html'),
    name='login'),
    re_path(r'^logout/$',auth_view.LogoutView.as_view(),name='logout'),
    re_path(r'signup/$',views.signup.as_view(),name='signup'),

]
