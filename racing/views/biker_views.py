from racing.base.base_views import PrivateGetAPIView
from racing.constants import Result
from racing.mangers import biker_manager
from racing.models import Biker


class BikerGetProfileView(PrivateGetAPIView):
    def __init__(self):
        PrivateGetAPIView.__init__(self)

    def process(self, data):
        self.validate_data(data)
        biker = Biker.objects.filter(id=self.user_id).first()
        if biker:
            return Result.SUCCESS, biker_manager.generate_biker_response(biker)

        return Result.ERROR_SERVER, {}

    def validate_data(self, data):
        pass
