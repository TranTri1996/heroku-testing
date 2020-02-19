from racing.base.base_views import PrivateGetAPIView
from racing.constants import Result
from racing.mangers import biker_manager
from racing.models import Biker


class BikerGetProfileView(PrivateGetAPIView):

    def process(self, data):
        try:
            biker = Biker.objects.filter(id=self.user_id).first()
            if biker:
                return Result.SUCCESS, biker_manager.generate_biker_response(biker)

            return Result.ERROR_USER_IS_NOT_FOUND, {}

        except Exception as e:
            print(str(e))
            return Result.ERROR_SERVER, str(e)

