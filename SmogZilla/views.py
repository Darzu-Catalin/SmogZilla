import http

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Contact
# Create your views here.



import telegram

token = '7118627124:AAH3YixJziuJ3CZDfUS0HY-0vvr2x87v5pw'
chat_id = '5614463571'


def index(request):
    return render(request, 'index.html')

def addReview(request):
    name = request.POST['name']
    email = request.POST['email']
    comment = request.POST['comment']
    review = Contact(name=name, email=email, comment=comment)
    review.save()
    request.close()

    #bot = Bot(token=TELEGRAM_BOT_TOKEN)
    #chat_id = '5614463571'
    #message_data = 'test'
    #bot.send_message(chat_id=chat_id, text=message_data)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



def app(request):
    return render(request, 'app.html')
