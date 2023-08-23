from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_auth.views import LogoutView
from rest_framework.views import APIView
from .serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_404_NOT_FOUND
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView

# Create your views here.
class LogoutView(LogoutView):
    authentication_classes = [TokenAuthentication]
    pass


class CreateUserProfileView(ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user']

    def post(self, request):
        try:
            serializer = UserProfileSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        
class UpdateUserProfileView(APIView):
    def put(self,request, pk):
        try:
            profile = UserProfile.objects.get(id = pk)
            serializer = UserProfileSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status= HTTP_404_NOT_FOUND)
        except Exception as e: return Response({'error': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)
        except profile.DoesNotExist:
            return Response({'error': 'Profile image was not added; Add Profile Image!'}, status= HTTP_404_NOT_FOUND)

    def patch(self,request, pk):
        try:
            profile = UserProfile.objects.get(id=pk)
            serializer = UserProfileSerializer(data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status= HTTP_404_NOT_FOUND)
        except Exception as e: return Response({'error': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)
        except profile.DoesNotExist:
            return Response({'error': 'Profile image was not added; Add Profile Image!'}, status= HTTP_404_NOT_FOUND)


class DeleteUserProfileView(APIView):
    def delete(self, request, pk):
        profile = UserProfile.objects.get(id = pk)
        try:
            if not profile:
                return Response({'error': 'Cart Id not found...'}, status = HTTP_404_NOT_FOUND)
            else:
                profile.delete()
                return Response({'success': 'profile image have been deleted successful...'}, status = HTTP_200_OK)
        except Exception as e: return Response({'error': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)
        except UserProfile.DoesNotExist: return Response({'error': 'Profile image was not added; Add Profile Image!'}, status=HTTP_404_NOT_FOUND)
