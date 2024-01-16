from django.urls import path
from . import views


#http://localhost:8000/account/login -> Login page
#http://localhost:8000/account/register -> Register page
#http://localhost:8000/account/logout -> Logout page

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/',views.logout_request,name='logout'),
    path('profile/',views.profile,name='profile'),
]