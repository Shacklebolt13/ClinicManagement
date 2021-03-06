from django.urls import path
from django.urls.conf import include
from . import views,apiviews


urlpatterns = [
    path('home',views.home,name='site'),
    path('book',views.book,name='book'),
    path('appointments',views.seeApps,name='appis'),
    path('pay',views.pay,name='pay'),
    path('paydone',views.paydone,name='paydone'),
    path('appois',apiviews.Appointment.as_view()),
]
