from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'ipapp'

urlpatterns = [

    
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("table/", views.table, name= "table"),
    path('chart/', views.chart, name='chart'),
    path('index2/', views.index2, name='index2'),
    path('', views.homepage, name='homepage'),
   
]


urlpatterns += staticfiles_urlpatterns()
