from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   # return HttpResponse("Rango says hey there partner! <a href='http://127.0.0.1:8000/rango/about/'>About</a>")
   context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
   return render(request, 'rango/index.html', context=context_dict)
def about(request):
  #  return HttpResponse("Rango says here is the about page. <a href='http://127.0.0.1:8000/'>Index</a>")
    context_dict = {'boldmessage': 'Sofia'}
    return render(request, 'rango/about.html', context=context_dict)