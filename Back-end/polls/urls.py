from django.urls import path

from . import views

urlpatterns = [
    path('<str:attributes>', views.detail, name='index'),
]