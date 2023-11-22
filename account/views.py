from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, serializers
from rest_framework.decorators import api_view

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK

from account.models import User
# from account.models import User
from account.serializer import RegisterSerializer, UserSerializer, SignupSerializer, UserLoginSerializer
from configs.response import createResponse, getResponse, loginResponse


# from configs.response import loginResponse


# from configs.response import  loginResponse


# Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(["POST", "GET"])
def signUp(request):
    if request.method == 'POST':
        # check_email = get_user_model().objects.filter(email='natnael@gmail.com').exists()
        check_username = get_user_model().objects.filter(username=request.data['username'])
        check_email = get_user_model().objects.filter(email=request.data['email'])
        email_serializer = UserSerializer(check_email, many=True)
        username_serializer = UserSerializer(check_username, many=True)

        if username_serializer.data != [] and email_serializer.data != []:
            return JsonResponse({
                "errors": [
                    "Email is taken", "Username is taken"
                ]
            })
        if email_serializer.data:
            return JsonResponse({
                "error": [
                    "Email is taken"
                ]
            })
        if username_serializer.data:
            return JsonResponse({
                "error": [
                    "Username is taken"
                ]
            })
        if request.data.get("is_superuser") == True or request.data.get("is_staff") == True:
            return JsonResponse({
                "error": [
                    "Unauthorized"
                ]
            }, status=403)

        if request.data['password'] != request.data['password2']:
            password_error = "Passwords don't match."
            return JsonResponse({
                "error": password_error
            }, status=400)
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return createResponse(serializer.data)

    if request.method == "GET":
        user = get_user_model().objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse({"data": serializer.data}, status=200)


@csrf_exempt
@api_view(["POST", 'GET'])
def login(request):
    if request.method == "POST":
        email = request.data.get("email")
        username = request.data.get("username")
        password = request.data.get("password")
        print('email', email)
        try:
            if email is not None:
                user = get_user_model().objects.get(email=email)
                user_data = User.objects.get(email=email)
            if username is not None:
                user = get_user_model().objects.get(username=username)
        except get_user_model().DoesNotExist:
            return JsonResponse({"data": "User Not Found"}, status=400)

        if not user.check_password(password):
            return JsonResponse({"data": "Invalid Credential"}, status=400)

        if user.check_password(password):
            token, _ = Token.objects.get_or_create(user=user)
            # return loginResponse(token.key)
            # return JsonResponse({"message": "User Logged In", "data": user})
            serializer = UserLoginSerializer(user_data)
            serializer.data.update(serializer.data)
            # all_dict.append({"token":token.key})
            return loginResponse(all_dict, token.key)

    return JsonResponse({"data": "User Not Logged in"})
