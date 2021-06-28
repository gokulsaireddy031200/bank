from django.urls import path
from spa.views import Testing
from . import views

urlpatterns = [
    path('get_records/',views.get_records,name='get_records'),
    path('',views.bookmarks ,name='bookmarks'),
    
    ]