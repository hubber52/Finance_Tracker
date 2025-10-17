from django.shortcuts import render
from ..Serials.serializer import UserSerializer, CustomUserProfile, CustomUserSerializer, UserLoginSerializer
from ..models import CustomUserProfile
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

CustomUser = get_user_model

class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user)
            data = serializer.data
            data['password'] = {" "}
            #data['tokens'] = {"refresh": str(token), "access": str(token.access_token)}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class UserLoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        serializer = CustomUserSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data['password'] = "Accepted"
        #data['tokens'] = {'refresh':str(token), 'access':str(token.access_token)}
        data['refresh'] = str(token)
        data['access'] = str(token.access_token)
        return Response(data, status=status.HTTP_202_ACCEPTED)

        #return Response({'error': 'Invalid Credentails'}, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            request_token = request.data['refresh']
            token = RefreshToken(request_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class UserAPIView(APIView):
    """
    Get, Update user information
    """

    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user