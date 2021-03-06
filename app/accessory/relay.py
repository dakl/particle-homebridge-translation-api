from requests import post

from app import config
from .base import Accessory


class Relay(Accessory):
    STATE_MAP = {
        1: 'HIGH',
        0: 'LOW',
    }

    def __init__(self,
                 name,
                 internal_id,
                 device_id=None,
                 access_token=None,
                 base_url=None,
                 headers=None):
        self.name = name
        self.internal_id = internal_id
        self.device_id = device_id or config.RELAY_HUB_DEVICE_ID
        self.access_token = access_token or config.PARTICLE_ACCESS_TOKEN
        self.base_url = base_url or config.PARTICLE_BASE_URL
        self.headers = headers or {
            "Content-type": "application/x-www-form-urlencoded"
        }
        if not self.device_id:
            raise ValueError(
                'Need to set RELAY_HUB_DEVICE_ID in the environment')
        if not self.access_token:
            raise ValueError(
                'Need to set PARTICLE_ACCESS_TOKEN in the environment')
        if not self.base_url:
            raise ValueError(
                'Need to set PARTICLE_BASE_URL in the environment')

    def _get_url(self, endpoint):
        return f"{self.base_url}/{self.device_id}/{endpoint}"

    def _set_state(self, state_string):
        url = self._get_url(endpoint='relay')
        payload = {
            'access_token': self.access_token,
            'args': f'{self.internal_id},{state_string}'
        }
        return post(url, data=payload, headers=self.headers).json()

    def set_state(self, state: int) -> bool:
        state_string = self.STATE_MAP.get(state, None)
        if state_string:
            response = self._set_state(state_string)
            if response.get('return_value') == 1:
                return True
            else:
                return False
        else:
            return False

    def get_state(self) -> int:
        url = self._get_url('state')
        payload = {
            'access_token': self.access_token,
            'args': f'{self.internal_id}'
        }
        resp = post(url, data=payload, headers=self.headers).json()

        return int(resp.get('return_value'))
