from django.urls import path, include
from .views import LogoutView, CreateUserProfileView, UpdateUserProfileView, DeleteUserProfileView

urlpatterns = [
    path('auth/logout', LogoutView.as_view(), name='logout'),
    path('create/profile', CreateUserProfileView.as_view(), name='create_profile'),
    path('update/<str:pk>/profile', UpdateUserProfileView.as_view(), name='update_profile'),
    path('delete/<str:pk>/profile', DeleteUserProfileView.as_view(), name='delete_profile'),
    path('', include('media_app.urls'))
]