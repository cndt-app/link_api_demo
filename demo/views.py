import datetime

from django.shortcuts import redirect
from django.views.generic import FormView, RedirectView, TemplateView

from .conduit_api import ConduitAPI, ConduitUserAPI
from .forms import AddNewUserForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = AddNewUserForm

    def get_context_data(self, **kwargs):
        users = ConduitAPI().get_users()

        return {
            'users': users,
        }

    def form_valid(self, form):
        return redirect('user_info', guid=form.cleaned_data['guid'])


class UserInfo(TemplateView):
    template_name = 'user_info.html'

    def get_context_data(self, guid: str, **kwargs):
        user_token = ConduitAPI().get_user_token(guid)
        credentials = ConduitUserAPI(user_token).get_credentials()

        return {
            'user_guid': guid,
            'credentials': credentials,
        }

class ConnectView(RedirectView):

    def get_redirect_url(self, guid: str, driver_id: str, *args, **kwargs):
        user_token = ConduitAPI().get_user_token(guid)
        connect_url = ConduitUserAPI(user_token).get_connect_url(driver_id)

        return connect_url


class DataLakeView(TemplateView):
    template_name = 'data.html'

    def get_context_data(self, guid: str, driver_id: str, account_id: str, **kwargs):
        user_token = ConduitAPI().get_user_token(guid)
        today = datetime.date.today()

        data = ConduitUserAPI(user_token).get_data_urls(
            driver_id,
            date_from=today - datetime.timedelta(days=3),
            date_to=today,
            account_id=account_id,
        )

        return {
            'data': data,
        }
