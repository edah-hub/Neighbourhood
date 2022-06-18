from django.shortcuts import render, redirect,HttpResponseRedirect
from django.conf import settings
from django.templatetags.static import static
from django.http import HttpResponse, Http404
import datetime as dt
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages


# Create your views here.
def index(request):


    return render(request, 'index.html')
