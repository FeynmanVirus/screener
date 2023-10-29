from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('screener/<str:title>', views.screener, name='screener'),
    path('pricing/', views.pricing, name='pricing'),
    path('pay/<int:price>', views.pay, name='pay'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('contact', views.contact, name='contact'),
    path('terms', views.terms, name='terms'),
]