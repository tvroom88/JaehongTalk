# Create your views here.
#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import *
from Main.models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf

import simplejson

# 처음 들어갈때의 페이지
@csrf_exempt
def main_page(request):
    return render_to_response('main_page.html', RequestContext(request, {'id': 12}))

# 로그아웃할때 main_page로 돌가가게 함
@csrf_exempt
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@csrf_exempt
def new_member(request):
    return render_to_response('NewPerson.html')

@csrf_exempt
def UserIdentitySave(request):

    user_id = request.POST['newUserId']
    user_password = request.POST['newUserPassWord']

    memberIdentity = Member(username=user_id, password=user_password)
    memberIdentity.save()


    return render_to_response('NewPerson.html')


@csrf_exempt
def talk_page(request):
      return render_to_response('talk.html')

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('passwrod', '')

    user = Member(username=username, password=password)

    if user is not None:
        return HttpResponseRedirect()
    else:
        return HttpResponseRedirect()

#HOON
@csrf_exempt
def login(request):
    #Get Parameter
    user_id = request.POST['user_id']
    user_password = request.POST['user_password']
    print user_id
    print user_password
    user = auth.authenticate(username=user_id, password=user_password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else :
        result = {'result':'0'}
        return HttpResponse(simplejson.dumps(result), 'application/json')

@csrf_exempt
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@csrf_exempt
def register(request):

    username = request.POST['newUserId']
    password = request.POST['newUserPassWord']
    try :
        User.objects.get(username=username)
        return HttpResponse("이미 있는 아이디 입니다")
    except :
        users = User.objects.create_user(username=username, password=password)
        if users is not None:
            return HttpResponseRedirect('/')






