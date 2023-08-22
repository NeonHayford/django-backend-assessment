from django.urls import path, include

urlpatterns = [
    # path('auth/logout', LogoutView.as_view(), name='logout'),
    path('', include('user_channels.urls')),
    path('', include('user_groups.urls'))
]