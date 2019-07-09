from django.conf.urls import url

from . import views



urlpatterns = [

    url('show_details/', views.show_details, name='show_details'),
    url('get_user_details/', views.get_user_details, name='get_user_details'),
    url('register/', views.register, name='register')
]