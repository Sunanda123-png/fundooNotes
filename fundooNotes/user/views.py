import json
import logging

from django.contrib.auth.models import auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User


logging.basicConfig(filename="views.log", filemode="w")


@csrf_exempt
def user_registration(request):
    """
    this method is created for user registration
    :param request: web request for user details storing
    :return: response
    """
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            user_name = data.get("user_name")
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            age = data.get("age")
            password = data.get("password")
            email = data.get("email")

            if User.objects.filter(username=user_name).exists():
                return JsonResponse({"message":"This user name is already taken"})
            elif User.objects.filter(email=email).exists():
                return JsonResponse({"message":"This email is already taken"})
            else:
                user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name, age=age,password=password, email=email, is_verified=0)
                user.save()
                return JsonResponse({"message":"data added successfully","data":data})
    except Exception as e:
        logging.error(e)
        print(e)


@csrf_exempt
def user_login(request):
    """
    this method is created for user_login
    :param request: web request for login
    :return:
    """
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            print(json.loads(request.body))
            user=auth.authenticate(username=data.get("user_name"), password=data.get("password"))
            if user is not None:
                return JsonResponse({"message":"User is valid", "data":data})
            else:
                return JsonResponse({"message": "User is invalid"})
    except Exception as e:
        logging.error(e)