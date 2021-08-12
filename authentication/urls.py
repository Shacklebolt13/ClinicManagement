from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('confirm',views.confirm,name='confirm'),
    path('signout',views.signout,name='signout'),
]
