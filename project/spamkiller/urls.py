from django.urls import path
from . import views

urlpatterns = [
    path('callback', view.callback)
]