import os


class Config:
    PARTICLE_BASE_URL = 'https://api.particle.io/v1/devices'
    RELAY_HUB_DEVICE_ID = os.getenv('RELAY_HUB_DEVICE_ID')
    PARTICLE_ACCESS_TOKEN = os.getenv('PARTICLE_ACCESS_TOKEN')
