from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ChannelSerializer, ChannelProfileSerializer, ChannelPostSerializer, PostLikesSerializer
from rest_framework.filters import SearchFilter
from .models import Channel, ChannelProfile, ChannelPost, ChannelPostLikes
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.
class CreateChannelView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['Channel_name']

    def post(self, request):
        try:
            serializer = ChannelSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        
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
    permission_classes = [IsAuthenticatedOrReadOnly]
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


class UpateChannelProfileView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ChannelProfile.objects.all()
    serializer_class = ChannelProfileSerializer

    @method_decorator(cache_page(60*60*24))
    def put(self, request, image_id, channel_id):
        try:
            channel = ChannelProfile.objects.get(id=image_id, channel_id=channel_id)
            serializer = ChannelProfileSerializer(channel, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status= HTTP_404_NOT_FOUND)
        except ChannelProfile.DoesNotExist:
            return Response({'status': 'Channel profile does not exist'}, status= HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

    @method_decorator(cache_page(60*60*24))
    def patch(self, request, image_id, channel_id):
        try:
            channel = ChannelProfile.objects.get(id=image_id, channel_id=channel_id)
            serializer = ChannelProfileSerializer(channel, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status= HTTP_400_BAD_REQUEST)
        except ChannelProfile.DoesNotExist:
            return Response({'status': 'Channel profile does not exist'}, status= HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)     


class DeleteChannelProfileView(DestroyAPIView):
    def delete(self, request, image_id, channel_id):
        try:
            channel = ChannelProfile.objects.get(id=image_id, channel_id=channel_id)
            if channel:
                channel.delete()
                return Response({'success': 'Channel profile have been deleted successfully'}, status=HTTP_204_NO_CONTENT)
            return Response({'error': 'Channel profile was not add to the channel'}, status = HTTP_404_NOT_FOUND)
        except ChannelProfile.DoesNotExist:
            return Response({'status':'Channel do not exist'}, status = HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)



class CreateChannelPostView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
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


class DeleteChannelPostView(DestroyAPIView):
    queryset = ChannelPost.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
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



class AddChannelPostLikeView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ChannelPostLikes.objects.all()
    serializer_class = PostLikesSerializer

    def  post(self, request, *args, **kwargs):
        try:
            serializer = PostLikesSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


class RemoveChannelPostLikeView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def delete(self, request, likes):
        try:
            post = ChannelPostLikes.objects.get(id=likes)
            if post:
                post.delete()
                return Response({'success': 'likes post have been deleted successfully'}, status=HTTP_204_NO_CONTENT)
            return Response({'error': 'Channel profile was not add to the channel'}, status = HTTP_404_NOT_FOUND)
        except ChannelPostLikes.DoesNotExist:
            return Response({'status':'likes post do not exist'}, status = HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

    