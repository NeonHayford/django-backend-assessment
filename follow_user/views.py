from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import FollowerSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class FollowersView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request):
        def post(self, request):
            try:
                serializer = FollowerSerializer(data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status = HTTP_200_OK)
            except Exception as e: 
                return Response({'error': str(e)}, status= HTTP_500_INTERNAL_SERVER_ERROR)