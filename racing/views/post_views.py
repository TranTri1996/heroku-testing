from racing.base.base_views import GetAPIView, PostAPIView
from racing.mangers.post_manager import generate_post_response
from racing.models.models import Post
from racing.constants import Result


class PostListAllView(GetAPIView):

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

    def process(self, data):
        post = Post.objects.create(author_id=data["author_id"],
                                   like_number=data["like_number"],
                                   share_number=data["share_number"],
                                   view_number=data["view_number"],
                                   title=data["title"],
                                   description=data["description"],
                                   images=data["images"],
                                   comment_ids=data["comment_ids"])

        return Result.SUCCESS, {"id": post.id}
