from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .models import Book,FeedBack
from .forms import FeedBackFrom
from django.urls import reverse
from django.views import View
from django.shortcuts import get_object_or_404
# Create your views here.


class FeedBackView(View):
    def get(self,request):
        form = FeedBackFrom()
        return render(request, "books/feedback.html", context={'form': form})

    def post(self,request):
        form = FeedBackFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/wear")
        return render(request, "books/feedback.html", context={'form': form})


def index(request):
    if request.method == 'POST':
        form = FeedBackFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("wer"))
    else:
        form = FeedBackFrom()
    return render(request,"books/feedback.html",context={'form':form})


class DoneView(View):
    def get(self,request):
        return render(request, "books/wer.html")


def wer(request):
    return render(request,"books/wer.html")


class UpdateFeedbackView(View):
    def get(self, request, id_feedback):
        feed = get_object_or_404(FeedBack,id = id_feedback)
        form = FeedBackFrom(instance=feed)
        return render(request, 'books/feedback.html', context={'form': form})

    def post(self, request, id_feedback):
        feed = FeedBack.objects.get(id=id_feedback)
        form = FeedBackFrom(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
        form = FeedBackFrom(instance=feed)
        return render(request, 'books/feedback.html', context={'form': form})

def getAllBooks(request):
    books = Book.objects.order_by('title')
    context = {"allBook":books}
    return render(request,"books/allbooks.html",context)


def getBook(request,movie_slug:str):
    book = get_object_or_404(Book,slug = movie_slug)
    context = {'book':book}

    return render(request,"books/getBook.html",context)