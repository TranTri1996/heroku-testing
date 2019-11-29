from rest_framework.views import APIView
from racing.models.models import Post
from racing.serializers.post_serializers import PostSerializer
from rest_framework.response import Response


class PostListAllView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)


class PostCreateView(APIView):

    def post(self, request):
        data = request.data
        Post.objects.create(id=data["id"],
                            biker_id=data["biker_id"],
                            status=data["status"])

        return Response({"result": "success"})
