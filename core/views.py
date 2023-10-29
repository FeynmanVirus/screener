import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from datetime import date, timedelta

from .forms import *
from .models import * 

def index(request):
    return render(request, 'core/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:index')
        else:
            print('invalid form')
    else:
        form = SignUpForm()   
    return render(request, 'core/signup.html', {'form': form})

def log_in(request):
    error = False
    if request.user.is_authenticated:
        return redirect('core:index')
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)  
                return redirect('core:index')
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'core/login.html', {'form': form, 'error': error})


def log_out(request):
    logout(request)
    return redirect('core:login')


# data = {
#   'scan_clause': '( {cash} ( latest volume >= 100000 and latest close >= 100 and latest close >= latest ema( latest close , 20 ) and latest close >= latest close and latest "close - 1 candle ago close / 1 candle ago close * 100" <= 5 and ( latest high - latest close ) / ( latest high - latest low ) <= 0.5 and latest ema( latest close , 9 ) >= latest ema( latest close , 20 ) ) )'
# }

def pay(request, price):
    if price == 699:
        price = 699*3
    elif price == 499:
        price = 499*12

    return render(request, 'core/pay.html', {
        'price': price
    })

def screener(request, title):
    if request.user.is_anonymous:
        return render(request, 'core/error.html')
    if not request.user.subscribed:
        return render(request, 'core/error.html')
    screeners = Screener.objects.all().values('title', 'clause')
    stocks = get_data(request, title)

    return render(request, 'core/screener.html', {
        'screeners': screeners,
        'stocks': stocks,
        'current': title,
    })


def get_data(request, title):
    print(title)
    data = {}
    with requests.Session() as s:
        data['scan_clause'] = Screener.objects.filter(title=title).values('clause')[0]['clause']
        print(data)
        r = s.get('https://chartink.com/screener/')
        soup = bs(r.content, 'lxml')
        s.headers['X-CSRF-TOKEN'] = soup.select_one('[name=csrf-token]')['content']
        r = s.post('https://chartink.com/screener/process', data=data).json()
        stocks = dict(r) 
        stocks = sorted(r['data'], key=lambda x: x["per_chg"], reverse=True)


        return stocks 
        
def pricing(request):
  return render(request, 'core/pricing.html')  

def contact(request):
    return render(request, 'core/contact.html')

def terms(request):
    return render(request, 'core/terms.html')