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
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

class UpateGroupView(UpdateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def put(self, request, pk, author_id):
        try:
            group = Group.objects.get(id=pk, author_id=author_id)
            serializer = GroupSerializer(group, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status= HTTP_404_NOT_FOUND)
        except Group.DoesNotExist:
            return Response({'status': 'Group-Chat does not exist'}, status= HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk, author_id):
        try:
            group = Group.objects.get(id=pk, author_id=author_id)
            serializer = GroupSerializer(group, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status= HTTP_400_BAD_REQUEST)
        except Group.DoesNotExist:
            return Response({'status': 'Group-Chat does not exist'}, status= HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteGroupView(DestroyAPIView):
    def delete(self, request, pk, author_id):
        try:
            group = Group.objects.get(id=pk, author_id=author_id)
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
    serializer_class = MessageSerializer
    filter_backends = [SearchFilter]
    search_fields = ['content', 'author']

    def post(self, request):
        try:
            serializer = MessageSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteChatMessageView(DestroyAPIView):
    def delete(self, request, pk, author_id):
        try:
            group = ChatMessage.objects.get(id=pk, author_id=author_id)
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
    search_fields = ['message', 'author']

    def post(self, request):
        try:
            serializer = CommentSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteCommentView(DestroyAPIView):
    def delete(self, request, comment_id, author_id):
        try:
            group = Comment.objects.get(id=comment_id, author_id=author_id)
            if group:
                group.delete()
                return Response({'success': 'comment to message have been deleted successfully'}, status=HTTP_204_NO_CONTENT)
            return Response({'error': 'comment to message have not been created'}, status = HTTP_404_NOT_FOUND)
        except Group.DoesNotExist:
            return Response({'status':'comment to message do not exist'}, status = HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)
        


class CreateReplyView(ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    filter_backends = [SearchFilter]
    search_fields = ['message', 'author']

    def post(self, request):
        try:
            serializer = ReplySerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteReplyView(DestroyAPIView):
    def delete(self, request, pk, author_id):
        try:
            group = Reply.objects.get(id=pk, author_id=author_id)
            if group:
                group.delete()
                return Response({'success': 'reply to comment have been deleted successfully'}, status=HTTP_204_NO_CONTENT)
            return Response({'error': 'reply to comment have not been created'}, status = HTTP_404_NOT_FOUND)
        except Group.DoesNotExist:
            return Response({'status':'reply to comment do not exist'}, status = HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)




class CreateMessageLikesView(ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = MessageLikes.objects.all()
    serializer_class = MessagelikesSerializer

    def post(self, request):
        try:
            serializer = MessagelikesSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteMessageLikesView(DestroyAPIView):
    def delete(self, request, pk, message_id):
        try:
            group = MessageLikes.objects.get(id=pk, chatmessage_id=message_id)
            if group:
                group.delete()
                return Response({'success': 'Group-Chat message have been deleted successfully'}, status=HTTP_204_NO_CONTENT)
            return Response({'error': 'Group-Chat message have not been created'}, status = HTTP_404_NOT_FOUND)
        except Group.DoesNotExist:
            return Response({'status':'Group-chat message do not exist'}, status = HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)


class CreateCommentLikesView(ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = CommentLikes.objects.all()
    serializer_class = CommentlikesSerializer

    def post(self, request):
        try:
            serializer = CommentlikesSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteCommentLikesView(DestroyAPIView):
    def delete(self, request, id, message_id):
        try:
            group = CommentLikes.objects.get(id=id, message_id=message_id)
            if group:
                group.delete()
                return Response({'success': 'comment to message have been deleted successfully'}, status=HTTP_204_NO_CONTENT)
            return Response({'error': 'comment to message have not been created'}, status = HTTP_404_NOT_FOUND)
        except Group.DoesNotExist:
            return Response({'status':'comment to message do not exist'}, status = HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)
        


class CreateReplyLikesView(ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ReplyLikes.objects.all()
    serializer_class = ReplylikesSerializer

    def post(self, request):
        try:
            serializer = ReplylikesSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteReplyLikesView(DestroyAPIView):
    def delete(self, request, pk, message_id):
        try:
            group = ReplyLikes.objects.get(id=pk, message_id=message_id)
            if group:
                group.delete()
                return Response({'success': 'reply to comment have been deleted successfully'}, status=HTTP_204_NO_CONTENT)
            return Response({'error': 'reply to comment have not been created'}, status = HTTP_404_NOT_FOUND)
        except Group.DoesNotExist:
            return Response({'status':'reply to comment do not exist'}, status = HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

                        