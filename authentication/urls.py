from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('practo_sign',views.pracSignin,name='psign'),
    path('price',views.price,name='price'),
]
