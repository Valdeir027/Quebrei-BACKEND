from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
import json as simplejson


# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, "auth/login.html")

    if request.method == "POST":
        data = simplejson.loads(request.body)

        user = authenticate(request, username=data.get('username'), password=data.get('password'))

        if user:
            auth_login(request=request, user=user)

            return JsonResponse({
                "sucess": "user autheticaded"
            })
        else:
            return JsonResponse({
                "error": "incorrect username or password"
            })
