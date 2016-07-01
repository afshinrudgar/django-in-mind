from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Place, User

# Create your views here.

def home(request):
  return HttpResponse('emtiaz home')


def place(request, uri):
  try:
    p = Place.objects.get(uri=uri)
    return HttpResponse("You're viewing place: %s" %p)
  except ObjectDoesNotExist:
    return HttpResponse("There is'nt such a place")


def user(request, username):
  try:
    u = User.objects.get(username=username)
    return HttpResponse("User: %s" %u)
  except ObjectDoesNotExist:
    return HttpResponse("There isn't such a user")