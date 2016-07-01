from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader

from .models import Place, User, Review

# Create your views here.

def home(request):
  latest_reviews = Review.objects.order_by('-date')[:10]
  # template = loader.get_template('website/index.html')
  context = {
    'latest_reviews': latest_reviews
  }
  # return HttpResponse(template.render(context, request))
  return render(request, 'website/index.html', context)


def place(request, uri):
  try:
    p = Place.objects.get(uri=uri)
    latest_reviews = Review.objects.filter(about=p).order_by('-date')[:10]
    return render(request, 'website/index.html', {
      'latest_reviews': latest_reviews
      })
  except ObjectDoesNotExist:
    raise Http404("There is'nt such a place")


def user(request, username):
  user = get_object_or_404(User, username=username)
  latest_reviews = user.review_set.order_by('-date')[:10]
  return render(
    request, 
    'website/index.html', 
    {'latest_reviews': latest_reviews}
  )


def login(req):
  if req.method == 'POST':
    print('username', req.POST['username'])
    print('password', req.POST['password'])
    return redirect('website:home')
  else:
    return render(req, 'website/login.html')