import json
import logging
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

logging.basicConfig(filename="views.log", filemode="w")


@csrf_exempt
def user_registration(request):
    """
    this method is created for user registration
    :param request: web request for user details sotoring
    :return: response
    """
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            user_name = data.get("user_name")
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            age = data.get("age")
            mobile = data.get("mobile")
            password = data.get("password")
            email = data.get("email")
            user = User(user_name=user_name, first_name=first_name, last_name=last_name, age=age, mobile=mobile,
                        password=password, email=email)
            user.save()
            return HttpResponse("Data stored successfully")
    except Exception as e:
        logging.error(e)


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
            user_name = data["user_name"]
            password = data["password"]

            if User.objects.filter(user_name=user_name, password=password):
                return HttpResponse("User is exist")
    except Exception as e:
        logging.error(e)