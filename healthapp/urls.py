
from django.contrib import admin
from django.urls import path
from healthapp import views

urlpatterns = [
    #path('what is typed in browser', views.function_name, name='name of the url, used for creating links in html'),
    
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('starter/', views.starter, name='starter'),

]
