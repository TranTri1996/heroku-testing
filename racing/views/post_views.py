from rest_framework.views import APIView
from racing.models.models import Post
from racing.serializers.post_serializers import PostSerializer
from rest_framework.response import Response


class PostListAllView(APIView):

    def get(self, request):
        params = request.query_params
        posts = Post.objects.all()
        if params.get("post_id"):
            posts = posts.filter(id=params["post_id"])
        if params.get("biker_id"):
            posts = posts.filter(biker_id=params["biker_id"])
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)


class PostCreateView(APIView):

    def post(self, request):
        data = request.data
        Post.objects.create(id=Post.objects.all().count() + 1,
                            biker_id=data["biker_id"],
                            status=data["status"])

        return Response({"result": "success"})
