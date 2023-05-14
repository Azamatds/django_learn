from django.urls import path
from horoscope import views


urlpatterns = [
    path('', views.index),
    path("type/",views.type_index),
    path("type/<str:type_name>/",views.get_signs_by_element,name="type-element"),
    path('<int:month>/<int:day>/',views.calculate_zodiak),
    path("<str:sign_of_zodiac>/",views.get_horoscope_by_sign , name = 'horoscope-name'),
    path('<sign_zodiac>/',views.get_info_about_sign_zodiac_by_number),

]