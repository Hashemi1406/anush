from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentReplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    reply_comments = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_reply_comments(self, object):
        result = object.reply_comments.all()
        return CommentReplaySerializer(instance=result, many=True).data
