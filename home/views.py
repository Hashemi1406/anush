from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment
from .serializers import PostSerializer,CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status


class Home(APIView):
    # permission_classes = [IsAuthenticated, ]

    def get(self, request):
        posts = Post.objects.all()
        ser_data = PostSerializer(instance=posts, many=True)
        return Response(data=ser_data.data)


class PostDetailView(APIView):

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        srz_data = PostSerializer(instance=post)
        return Response(srz_data.data, status=status.HTTP_200_OK)


class PostCreateView(APIView):
    def post(self, request):
        srz_data = PostSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePostView(APIView):
    def put(self, request, post_id):
        post = Post.objects.get(id=post_id)
        srz_data = PostSerializer(instance=post, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDeleteView(APIView):
    def delete(self, request, post_id):
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({'message':'post deleted!'}, status=status.HTTP_200_OK)


class CommentsView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        srz_data = CommentSerializer(instance=comments, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)


class CreateCommentsView(APIView):
    def post(self, request):
        srz_data = CommentSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.data, status=status.HTTP_400_BAD_REQUEST)


class UpdateCommentsView(APIView):
    def put(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        srz_data = CommentSerializer(instance=comment, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCommentsView(APIView):
    def delete(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return Response({'message': 'comment deleted!'}, status=status.HTTP_200_OK)





