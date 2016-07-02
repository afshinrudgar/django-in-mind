from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
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


class HomeView(generic.ListView):
  template_name = 'website/index.html'
  context_object_name = 'latest_reviews'

  def get_queryset(self):
    ''' return last 10 review of all '''
    return Review.objects.order_by('-date')[:10]


# useless generic view
# below views doesn't work :)

class PlaceView(generic.DetailView):
  model = Place
  template_name = 'website/index.html'


class UserView(generic.ListView):
  ''' 
  is this supposed to be a ListView or generic Views have some limitation
  or just I too noob for this?!
  '''
  template_name = 'website/index.html'
  context_object_name = 'latest_reviews'

  def get_queryset(self):
    ''' is there a way to get username here ans return a list of objects '''
    return User.objects.get(username=username).review_set.order_by('-date')[:10]

# end of useless views