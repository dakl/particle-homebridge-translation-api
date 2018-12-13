from typing import Dict

from app.accessory import Relay, Accessory

ACCESSORIES: Dict[int, Accessory] = {
    1:
    Relay(
        name='relay-hub-1',
        internal_id='r1'),
    2:
    Relay(
        name='relay-hub-2',
        internal_id='r2'),
    3:
    Relay(
        name='relay-hub-3',
        internal_id='r3'),
    4:
    Relay(
        name='relay-hub-4',
        internal_id='r4'),
    # 5:
    # Relay(
    #     name='lego-house-1',
    #     device_id=os.getenv('LEGO_HOUSE_DEVICE_ID'),
    #     access_token=os.getenv('PARTICLE_ACCESS_TOKEN'),
    #     internal_id='0',
    #     args_template='{pin},{state}',
    #     path='pin'),
    # 6:
    # Relay(
    #     name='lego-house-2',
    #     device_id=os.getenv('LEGO_HOUSE_DEVICE_ID'),
    #     access_token=os.getenv('PARTICLE_ACCESS_TOKEN'),
    #     internal_id='1',
    #     args_template='{pin},{state}',
    #     path='pin'),
    # 7:
    # Relay(
    #     name='lego-house-3',
    #     device_id=os.getenv('LEGO_HOUSE_DEVICE_ID'),
    #     access_token=os.getenv('PARTICLE_ACCESS_TOKEN'),
    #     internal_id='2',
    #     args_template='{pin},{state}',
    #     path='pin'),
    # 8:
    # Relay(
    #     name='lego-house-4',
    #     device_id=os.getenv('LEGO_HOUSE_DEVICE_ID'),
    #     access_token=os.getenv('PARTICLE_ACCESS_TOKEN'),
    #     internal_id='3',
    #     args_template='{pin},{state}',
    #     path='pin'),
}
