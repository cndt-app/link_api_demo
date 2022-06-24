import datetime
from typing import Any, Optional

import requests
from urllib.parse import urljoin

# dev url & token
CONDUIT_API_URL = "https://link-dev.getconduit.app"
CONDUIT_API_TOKEN = " place api key here "


class ConduitAPI:

    def get_users(self) -> str:
        res = self._request('users/', method='GET')
        return res.json()

    def get_user_token(self, user_guid: str) -> str:
        res = self._request('auth/token/', data={'guid': user_guid})
        return res.json()['token']

    @staticmethod
    def _request(path, method: str = 'POST', data: dict[str, any] = None):
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {CONDUIT_API_TOKEN}',
        }
        res = requests.request(method, urljoin(CONDUIT_API_URL, path), headers=headers, json=data)
        res.raise_for_status()

        return res


class ConduitUserAPI:

    def __init__(self, token: str):
        self._token = token

    def get_credentials(self) -> list[dict[str, Any]]:
        res = self._request('credentials/')
        return res

    def get_connect_url(self, driver_id: str) -> str:
        res = self._request(f'credentials/connect/{driver_id}/')
        return res['url']

    def get_data_urls(
        self, driver_id: str, date_from: datetime.date, date_to: datetime.date, account_id: Optional[id] = None,
    ) -> dict[str, list[str]]:
        data = {
            'driver_id': driver_id,
            'date_from': date_from.isoformat(),
            'date_to': date_to.isoformat(),
        }
        if account_id:
            data['account_id'] = account_id

        res = self._request('data_lake/', data)
        return res

    def _request(self, path: str, data: dict[str, any] = None) -> Any:
        headers = {
            'accept': 'application/json',
        }
        data = data or {}
        data['token'] = self._token

        res = requests.request('GET', urljoin(CONDUIT_API_URL, path), headers=headers, params=data)
        res.raise_for_status()

        return res.json()
