from django.urls import path
from week_days import views

urlpatterns = [
    path('<int:day>/', views.get_day_info_int),
    path('<str:day>/', views.get_day_info,name = 'week_day'),
]