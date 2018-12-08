from requests import post

from app.config import Config as config


class Accessory:
    name: str

    def __init__(self, name):
        self.name = name

    def set_state(self):
        raise NotImplementedError()

    def get_state(self):
        raise NotImplementedError()


class MockAccessory(Accessory):
    def set_state(self):
        return 0

    def get_status(self):
        return 0


class Relay(Accessory):
    STATE_MAP = {
        'on': 'HIGH',
        'off': 'LOW',
    }

    def __init__(self,
                 name,
                 internal_id,
                 device_id=None,
                 access_token=None,
                 headers=None):
        self.name = name
        self.internal_id = internal_id
        self.device_id = device_id or config.RELAY_HUB_DEVICE_ID
        self.access_token = access_token or config.PARTICLE_ACCESS_TOKEN
        self.headers = headers or {
            "Content-type": "application/x-www-form-urlencoded"
        }

    def _get_url(self, path):
        return f"{config.PARTICLE_BASE_URL}/{self.device_id}/{path}"

    def _set_state(self, internal_state):
            url = self._get_url(path='relay')
            payload = {
                'access_token': self.access_token,
                'args': f'{self.internal_id},{internal_state}'
            }
            return post(url, data=payload, headers=self.headers).json()

    def set_state(self, state):
        internal_state = self.STATE_MAP.get(state, None)
        if internal_state:
            response = self._set_state(internal_state)
            return {'status': response.get('return_value')}
        else:
            return {'status': -1, 'message': f'Unable to map state `{state} to an internal state.`'}

    def get_status(self):
        url = self._get_url('state')
        payload = {
            'access_token': self.access_token,
            'args': f'{self.internal_id}'
        }
        resp = post(url, data=payload, headers=self.headers).json()

        return {'status': resp.get('return_value')}
