"""
URL configuration for my_page project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from horoscope import views as views_horoscope
from week_days import views as views_week_days
from book_app import views as books
from gallery import views as  gallery
urlpatterns = [
    path("admin/", admin.site.urls),
    # path("horoscope/aries/",views.aries),
    # path("horoscope/taurus/",views.taurus),
    path("horoscope/", include("horoscope.urls")),
    path("todo_week/", include('week_days.urls')),
    path("",include("book_app.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
    path("gallery/",include("gallery.urls"))
]
