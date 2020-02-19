from racing.base.base_views import PrivateGetAPIView, PrivatePostAPIView
from racing.mangers.post_manager import generate_post_response
from racing.constants import Result
from racing.models import Post, Biker


class PostListAllView(PrivateGetAPIView):

    def process(self, data):
        pass
        # posts = list(Post.objects.all())
        # if data.get("biker_id"):
        #     posts = list(p for p in posts if p.biker_id == data["biker_id"])
        # if data.get("post_id"):
        #     posts = list(p for p in posts if p.biker_id == data["post_id"])
        # post_serializers = []
        # for p in posts:
        #     post_serializers.append(generate_post_response(p))
        #
        # return Result.SUCCESS, post_serializers


class PostCreateView(PrivatePostAPIView):

    def process(self, data):
        pass
    #     self.validate_data(data)
    #     post = Post.objects.create(biker_id=data["biker_id"],
    #                                title=data.get("title", ""),
    #                                description=data.get("description", ""),
    #                                is_active=data.get("is_active", 1))
    #
    #     return Result.SUCCESS, generate_post_response(post)
    #
    # def validate_data(self, data):
    #     if not data.get("biker_id"):
    #         self.response_json(Result.ERROR_REQUIRED_BIKER_ID, {})
    #     if not self.is_biker_existed(data["biker_id"]):
    #         self.response_json(Result.ERROR_BIKER_IS_NOT_EXISTED, {})

    def is_biker_existed(self, biker_id):
        biker = Biker.objects.filter(id=biker_id).first()

        return True if biker else False
