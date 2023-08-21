from django.urls import path, include
from .views import LogoutView

urlpatterns = [
    path('auth/logout', LogoutView.as_view(), name='logout'),
]