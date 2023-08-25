from django.shortcuts import render
from .models import Group, ChatMessage, Comment, Reply
from .serializers import *
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.status import *

# Create your views here.
class CreateGroupView(ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [SearchFilter]
    search_fields = ['group_name']

    def post(self, request):
        try:
            serializer = GroupSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            # return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

class UpateGroupView(UpdateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def put(self, request, pk, author):
        try:
            group = Group.objects.get(id=pk, author_id=author)
            serializer = GroupSerializer(group, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status= HTTP_404_NOT_FOUND)
        except Group.DoesNotExist:
            return Response({'status': 'Group-Chat does not exist'}, status= HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk, author):
        try:
            group = Group.objects.get(id=pk, author_id=author)
            serializer = GroupSerializer(group, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status= HTTP_400_BAD_REQUEST)
        except Group.DoesNotExist:
            return Response({'status': 'Group-Chat does not exist'}, status= HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteChannelView(DestroyAPIView):
    def delete(self, request, pk, author):
        try:
            group = Group.objects.get(id=pk, author_id=author)
            if group:
                group.delete()
                return Response({'success': 'Group-Chat have been deleted successfully'}, status=HTTP_204_NO_CONTENT)
            return Response({'error': 'Group-Chat have not been created'}, status = HTTP_404_NOT_FOUND)
        except Group.DoesNotExist:
            return Response({'status':'Group-chat do not exist'}, status = HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)


class CreateChatMessageView(ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    filter_backends = [SearchFilter]
    search_fields = ['content', 'author']

    def post(self, request):
        try:
            serializer = ChatMessageSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            # return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteChatMessageView(DestroyAPIView):
    def delete(self, request, pk, author):
        try:
            group = ChatMessage.objects.get(id=pk, author_id=author)
            if group:
                group.delete()
                return Response({'success': 'Group-Chat message have been deleted successfully'}, status=HTTP_204_NO_CONTENT)
            return Response({'error': 'Group-Chat message have not been created'}, status = HTTP_404_NOT_FOUND)
        except Group.DoesNotExist:
            return Response({'status':'Group-chat message do not exist'}, status = HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)


class CreateCommentView(ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['content', 'author']

    def post(self, request):
        try:
            serializer = CommentSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            # return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteCommentView(DestroyAPIView):
    def delete(self, request, comments_id, author):
        try:
            group = Comment.objects.get(id=comments_id, author_id=author)
            if group:
                group.delete()
                return Response({'success': 'comment to message have been deleted successfully'}, status=HTTP_204_NO_CONTENT)
            return Response({'error': 'comment to message have not been created'}, status = HTTP_404_NOT_FOUND)
        except Group.DoesNotExist:
            return Response({'status':'comment to message do not exist'}, status = HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)
        

class CreateCommentView(ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['content', 'author']

    def post(self, request):
        try:
            serializer = CommentSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            # return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteCommentView(DestroyAPIView):
    def delete(self, request, pk, author):
        try:
            group = Comment.objects.get(id=pk, author_id=author)
            if group:
                group.delete()
                return Response({'success': 'reply to comment have been deleted successfully'}, status=HTTP_204_NO_CONTENT)
            return Response({'error': 'reply to comment have not been created'}, status = HTTP_404_NOT_FOUND)
        except Group.DoesNotExist:
            return Response({'status':'reply to comment do not exist'}, status = HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)