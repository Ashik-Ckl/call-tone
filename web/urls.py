"""calltone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [

    path('',views.index),
    path('view_product_details/<str:category>/',views.product_details_view),
    path('cart/',views.cart),
    path('checkout/',views.checkout),
    path('order_send_to_whatsaapp/<str:name>/<str:address>/<str:phone>/',views.send_to_whatsapp),
    path('about/',views.about),
    path('contact/',views.contact)
]
