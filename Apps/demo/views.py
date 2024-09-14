from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
# Create your views here.


# class Index(View):
#     books = Book.objects.all()

#     #filter method
#     # select data by parameter value
#     # Book.objects.filter(parameter (is_published=True))

#     #get method
#     # select data, and retun single data
#     # Book.objects.get(parameter (id=2))

#     output = ""
#     for book in books:
#         output += f"Title book is {book.title} <br>"
    
#     def get(self, request):
#         return HttpResponse(self.output)


def index(request):
    datas = Book.objects.all()
    return render(request, 'index.html', {'datas': datas})