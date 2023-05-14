from django.urls import path, include
from . import views

urlpatterns = [
    path("load",views.LoadView.as_view())
]
