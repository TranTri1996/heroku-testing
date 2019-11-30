from rest_framework.views import APIView

from racing.base.base_views import GetAPIView, PostAPIView
from racing.mangers.post_manager import generate_post_response
from racing.models.models import Post
from racing.serializers.post_serializers import CreatePostSerializer, PostListParamSerializer
from racing.constants import Result


class PostListAllView(GetAPIView):
    class_serializer = PostListParamSerializer

    def process(self, data):
        posts = Post.objects.all()
        if data.get("post_id"):
            posts = posts.filter(id=data["post_id"])
        if data.get("biker_id"):
            posts = posts.filter(biker_id=data["biker_id"])

        post_responses = []
        for p in posts:
            post_responses.append(generate_post_response(p))

        return Result.SUCCESS, post_responses


class PostCreateView(PostAPIView):
    class_serializer = CreatePostSerializer

    def process(self, data):
        post = Post.objects.create(id=Post.objects.all().count() + 1,
                                   biker_id=data["biker_id"],
                                   status=data["status"])

        return Result.SUCCESS, {"id": post.id}
