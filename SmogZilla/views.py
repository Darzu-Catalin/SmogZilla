import http

from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.



import telegram

token = '7118627124:AAH3YixJziuJ3CZDfUS0HY-0vvr2x87v5pw'
chat_id = '5614463571'


def index(request):
    return render(request, 'index.html')

# def addReview(request):
#     name = request.POST['name']
#     email = request.POST['email']
#     comment = request.POST['comment']
#     review = Contact(name=name, email=email, comment=comment)
#     review.save()
#     request.close()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
def addReview(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        if name and email and comment:
            review = Contact(name=name, email=email, comment=comment)
            review.save()
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return HttpResponseBadRequest("Missing fields in the form")
    else:
        return HttpResponseBadRequest("Invalid request method")



def app(request):
    return render(request, 'app.html')
