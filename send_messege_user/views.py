# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from send_messege_user.models import UserMessage
from django.contrib.auth.models import User
from extuser.models import MyUser
# Create your views here.


def send_messege_user(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['id_user'])
        send_user = MyUser.objects.get(user=request.user.id)
        UserMessage(user_message=user, message=request.POST['text_messege'], from_user=send_user).save()
        return HttpResponse('message send')
    else:
        return HttpResponse('error')


def get_messege(request):
    messages = UserMessage.objects.filter(user_message=request.user.id, read=False)
    return HttpResponse(JsonResponse({"new_message": len(messages)}))


def get_new_message_html(request):
    messages = UserMessage.objects.filter(user_message=request.user.id, read=False)
    return render(request, 'send_messege_user/message_user.html', {"messages": messages})


def get_text_message(request):
    id_mes = request.GET['id_mes'].split('-')[-1]
    message = UserMessage.objects.get(id=id_mes)
    message = JsonResponse({
        "from_fn": message.from_user.user.first_name,
        "from_ln": message.from_user.user.last_name,
        "time": message.time_message,
        "text_message": message.message
        })
    return HttpResponse(message)