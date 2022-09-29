import datetime

from django.shortcuts import redirect
from django.views.generic import FormView, RedirectView, TemplateView

from .conduit_api import ConduitAPI, ConduitCompanyAPI
from .forms import AddNewCompanyForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = AddNewCompanyForm

    def get_context_data(self, **kwargs):
        companies = ConduitAPI.get_companies()
        return {'companies': companies}

    def form_valid(self, form):
        ConduitAPI.create_company(form.cleaned_data['company_id'])
        return redirect('company_info', company_id=form.cleaned_data['company_id'])


class CompanyInfo(TemplateView):
    template_name = 'company_info.html'

    def get_context_data(self, company_id: str, **kwargs):
        company = ConduitAPI().get_company(company_id, include_connections=True)
        return {
            'company': company,
        }


class ConnectView(RedirectView):
    def get_redirect_url(self, company_id: str, integration_id: str, *args, **kwargs):
        token = ConduitAPI.get_token(company_id)
        return ConduitCompanyAPI(token).get_connect_url(integration_id)


class DataLakeView(TemplateView):
    template_name = 'data.html'

    def get_context_data(self, company_id: str, integration_id: str, account: str, **kwargs):
        token = ConduitAPI.get_token(company_id)
        today = datetime.date.today()

        data = ConduitCompanyAPI(token).get_data_urls(
            integration_id,
            date_from=today - datetime.timedelta(days=3),
            date_to=today,
            account=account,
        )
        return {'data': data}
