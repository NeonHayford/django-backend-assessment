from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_auth.views import LogoutView

# Create your views here.
class LogoutView(LogoutView):
    authentication_classes = [TokenAuthentication]
    pass