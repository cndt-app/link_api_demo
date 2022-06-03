import datetime
from django.views.generic import TemplateView, RedirectView

from .conduit_api import EXAMPLE_USER_GUID, ConduitAPI, ConduitUserAPI


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        user_token = ConduitAPI().get_user_token(EXAMPLE_USER_GUID)
        credentials = ConduitUserAPI(user_token).get_credentials()

        return {
            'user_guid': EXAMPLE_USER_GUID,
            'credentials': credentials,
        }


class ConnectView(RedirectView):

    def get_redirect_url(self, driver_id: str, *args, **kwargs):
        user_token = ConduitAPI().get_user_token(EXAMPLE_USER_GUID)
        connect_url = ConduitUserAPI(user_token).get_connect_url(driver_id)

        return connect_url


class DataLakeView(TemplateView):
    template_name = 'data.html'

    def get_context_data(self, driver_id: str, account_id: str, **kwargs):
        user_token = ConduitAPI().get_user_token(EXAMPLE_USER_GUID)
        today = datetime.date.today()
        start_day = today - datetime.timedelta(days = 3)

        data = ConduitUserAPI(user_token).get_data_urls(driver_id, date_from=start_day, date_to=today, account_id=account_id)

        return {
            'data': data,
        }
