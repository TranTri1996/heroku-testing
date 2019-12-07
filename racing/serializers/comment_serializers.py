from rest_framework_mongoengine.serializers import DocumentSerializer

from racing.models.models import Comment


class CommentSerializer(DocumentSerializer):
    class Meta:
        model = Comment
        depth = 2
        fields = '__all__'
