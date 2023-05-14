from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.getAllBooks),
    path("movie/<str:movie_slug>/", views.getBook, name='book-deital'),
    path("feedback/", views.index, name="feedback"),
    path("feedback/<int:id_feedback>/", views.UpdateFeedbackView.as_view()),
    path("wer/", views.wer, name="wer"),

]
