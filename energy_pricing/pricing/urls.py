from django.urls import path
from . import views

urlpatterns = [
    path('', views.pricing_dashboard, name='pricing_dashboard'),
    path('update_price', views.update_price, name='update_price'),
]
