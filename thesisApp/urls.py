from django.urls import path
from . import views


#http://localhost:8000/ -> Home page
#http://localhost:8000/home -> Home page
#http://localhost:8000/thesis -> Thesis page
#http://localhost:8000/thesis/1 -> Thesis Detail page
#http://localhost:8000/thesis/new -> New Thesis Request page


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('thesis/', views.thesis, name='thesis'),
    path('thesis/<int:thesis_id>/', views.thesis_detail, name='thesis_detail'),
    path('thesis/new/', views.new_thesis_request, name='new_thesis_request'),
]
