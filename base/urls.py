from django.urls.conf import path

from base import views

urlpatterns = [
    path('', views.base, name='base'),
]

