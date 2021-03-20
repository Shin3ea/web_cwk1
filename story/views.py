from django.views.decorators.http import require_http_methods
# from django.contrib.auth.decorators import method_decorator
from django.shortcuts import render
from django.http import (HttpResponse,Http404,HttpResponseBadRequest)
from .models import Author,Story
from django.views.decorators.csrf import csrf_exempt
import json

# @require_http_methods(["POST"])
@csrf_exempt
def HandleLoginRequest(request):
  # BEGIN_LOGIN
  # """""""""""
  # BEGIN_BASIC_CHECK
  # +++++++++++++++++
  #  Wrong request method
  #  ^^^^^^^^^^^^^^^^^^^^
  if request.method!='POST':
    badResponse = "{method} Not Allowed".format(method=request.method)
    return HttpResponseBadRequest(badResponse,content_type="text/plain",status=405)
  #  Payload is empty
  #  ^^^^^^^^^^^^^^^^
  if not request.POST:
    return HttpResponse("EMPTY CONTENT",content_type="text/plain",status=205)
  #  Key values are not matched
  #  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  if (not 'username' in request.POST) or (not 'password' in request.POST):
    NotKeyValue="Require the key [username, password]"
    return HttpResponse(NotKeyValue,content_type="text/plain",status=205)
  # +++++++++++++++
  # END_BASIC_CHECK

  # Setup
  # ^^^^^
  un=request.POST.get('username')
  pw=request.POST.get('password')
  # Cannot find username
  # ^^^^^^^^^^^^^^^^^^^^
  if not Author.objects.filter(Username__exact=un):
    NotFoundAuthor=("'{username}' NOT REGISTERED").format(username=un)
    return HttpResponse(NotFoundAuthor,content_type="text/plain",status=205)
  # Wrong password with given username
  # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  if not Author.objects.filter(Username__exact=un,Password__exact=pw):
    WrongPassword=("'{password}' WRONG PASSWORD OF '{username}'").format(password=pw,username=un)
    return HttpResponse(WrongPassword,content_type="text/plain",status=205)
  # Login
  # ^^^^^
  return HttpResponse("Welcome to ml17x44z site!!!",content_type="text/plain",status=200)
  # """""""""
  # END_LOGIN

def HandleLogoutRequest(request):
  if request.method!='POST':
    badResponse = "{method} Not Allowed".format(method=request.method)
    return HttpResponseBadRequest(badResponse,content_type="text/plain",status=405)
  return HttpResponse("Bye-bye Butterfly!",content_type="text/plain",status=200)
  # return render(request)

# def HandlePostStoryRequest(request):

#   return render(request)

# def HandleGetStoriesRequest(request):

#   return render(request)

# def HandleDeleteStoryRequest(request):

#   return render(request)
