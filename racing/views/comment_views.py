from racing.base.base_views import GetAPIView
from racing.models.models import Comment
from racing.constants import Result


class CommentListView(GetAPIView):

    def process(self, data):
        pass
