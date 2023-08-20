from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class LogoutView(LogoutView):
    authentication_classes = [TokenAuthentication]
    pass