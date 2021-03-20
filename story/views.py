from django.views.decorators.http import require_http_methods
# from django.contrib.auth.decorators import method_decorator
from django.shortcuts import render
from django.http import (HttpResponse,Http404,HttpResponseBadRequest)
from .models import Author,Story
from django.views.decorators.csrf import csrf_exempt

# @require_http_methods(["POST"])
@csrf_exempt
def HandleLoginRequest(request):
  if request.method!='POST':
    badResponse = "This api cannot handle {method}".format(method=request.method)
    return HttpResponseBadRequest(badResponse,content_type="text/plain",status=400)
  return HttpResponse("Welcome to ml17x44z site!!!",content_type="text/plain",status=200)

# def HandleLogoutRequest(request):

#   return render(request)

# def HandlePostStoryRequest(request):

#   return render(request)

# def HandleGetStoriesRequest(request):

#   return render(request)

# def HandleDeleteStoryRequest(request):

#   return render(request)
