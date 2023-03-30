from django.shortcuts import render

# Create your views here.

from .documents import *

def home(request):
  q = request.GET.get('q')
  if q:
    samples = SampleDocument.search().query("match", title=q)
  else:
    samples = ''
  context = {
    'samples': samples
  }
  
  return render(request,"index.html", context=context)