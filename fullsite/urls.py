from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('home',views.home,name='site'),
    path('book',views.book,name='book'),

]
