from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ChannelSerializer, ChannelProfileSerializer, ChannelPostSerializer, PostLikesSerializer
from rest_framework.filters import SearchFilter
from .models import Channel, ChannelProfile, ChannelPost, ChannelPostLikes
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView


# Create your views here.
class CreateChannelView(ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['channel_name']

    def post(self, request):
        try:
            serializer = ChannelSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        except Channel.DoesNotExist:
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)

class UpateChannelView(UpdateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    def put(self, request, pk, author):
        try:
            channel = Channel.objects.get(id=pk, author_id=author)
            serializer = ChannelSerializer(channel, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status= HTTP_404_NOT_FOUND)
        except Channel.DoesNotExist:
            return Response({'status': 'Channel does not exist'}, status= HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk, author):
        try:
            channel = Channel.objects.get(id=pk, author_id=author)
            serializer = ChannelSerializer(channel, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status= HTTP_400_BAD_REQUEST)
        except Channel.DoesNotExist:
            return Response({'status': 'Channel does not exist'}, status= HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteChannelView(DestroyAPIView):
    def delete(self, request, pk, author):
        try:
            channel = Channel.objects.get(id=pk, author_id=author)
            if channel:
                channel.delete()
                return Response({'success': 'Channel have been deleted successfully'}, status=HTTP_204_NO_CONTENT)
            return Response({'error': 'Channel have not been created'}, status = HTTP_404_NOT_FOUND)
        except Channel.DoesNotExist:
            return Response({'status':'Channel do not exist'}, status = HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)


class CreateChannelProfileView(ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ChannelProfile.objects.all()
    serializer_class = ChannelProfileSerializer
    filter_backends = [SearchFilter]
    search_fields = ['channel_name']

    def post(self, request):
        try:
            serializer = ChannelProfileSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        except Channel.DoesNotExist:
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)

class UpateChannelProfileView(UpdateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ChannelProfile.objects.all()
    serializer_class = ChannelProfileSerializer

    def put(self, request, image, author):
        try:
            channel = ChannelProfile.objects.get(id=image, author_id=author)
            serializer = ChannelProfileSerializer(ChannelProfile, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status= HTTP_404_NOT_FOUND)
        except ChannelProfile.DoesNotExist:
            return Response({'status': 'Channel profile does not exist'}, status= HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, image, author):
        try:
            channel = ChannelProfile.objects.get(id=image, author_id=author)
            serializer = ChannelProfileSerializer(ChannelProfile, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status= HTTP_400_BAD_REQUEST)
        except Channel.DoesNotExist:
            return Response({'status': 'Channel profile does not exist'}, status= HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)     

class DeleteChannelProfileView(DestroyAPIView):
    def delete(self, request, image, author):
        try:
            channel = ChannelProfile.objects.get(id=image, author_id=author)
            if channel:
                channel.delete()
                return Response({'success': 'Channel profile have been deleted successfully'}, status=HTTP_204_NO_CONTENT)
            return Response({'error': 'Channel profile was not add to the channel'}, status = HTTP_404_NOT_FOUND)
        except ChannelProfile.DoesNotExist:
            return Response({'status':'Channel do not exist'}, status = HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)


class CreateChannelPostView(ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ChannelPost.objects.all()
    serializer_class = ChannelPostSerializer

    def post(self, request):
        try:
            serializer = ChannelPostSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        except ChannelPost.DoesNotExist:
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)

class DeleteChannelPostView(DestroyAPIView):
    queryset = ChannelPost.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ChannelPostSerializer

    def delete(self, request, post_id):
        try:
            post = ChannelPost.objects.get(id=post_id)
            if post:
                post.delete()
                return Response({'success': 'Channel profile have been deleted successfully'}, status=HTTP_204_NO_CONTENT)
            return Response({'error': 'Channel profile was not add to the channel'}, status = HTTP_404_NOT_FOUND)
        except ChannelPost.DoesNotExist:
            return Response({'status':'Channel do not exist'}, status = HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)


class AddChnnelPostLikeView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, likes):
        try:
            channel = ChannelPostLikes.objects.get(id=likes)
            serializer = PostLikesSerializer(channel, data = request.data)
            if serializer.is_valid():
                ChannelPostLikes.post = ChannelPostLikes.post['likes'] + 1
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status= HTTP_404_NOT_FOUND)
        except ChannelPostLikes.DoesNotExist:
            return Response({'status': 'Channel profile does not exist'}, status= HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)


class RemoveChannelPostLikeView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def delete(self, request, likes):
        try:
            post = ChannelPostLikes.objects.get(id=likes)
            ChannelPostLikes.post = ChannelPostLikes.post['likes'] - 1
            post.delete() 
            return Response({'success': 'Channel profile have been deleted successfully'}, status=HTTP_204_NO_CONTENT)
        except ChannelPostLikes.DoesNotExist:
            return Response({'status':'Channel do not exist'}, status = HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

    