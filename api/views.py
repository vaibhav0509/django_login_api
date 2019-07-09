# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import reverse


# Create your views here.

@csrf_exempt
@api_view(["GET"])
def show_details(request):
    username = request.data.get('username')
    data = { username : "Ohh. A valid User"}
    return Response(data)

@api_view(["POST"])
@csrf_exempt
@permission_classes([AllowAny, ])
def get_user_details(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response('error :' 'Enter the correct the username or password')
    user = authenticate(username=username, password=password)
    if not user:
        return Response('error :''Not a valid user')
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})

def register(request):
    #
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'api/register.html ', {'form': form})

def base(request):
    return Response(request, 'api/login.html')