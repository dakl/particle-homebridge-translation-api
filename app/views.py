import logging

from flask import abort, jsonify, request

from app.accessories import ACCESSORIES
from app.setup import app

logger = logging.getLogger(__name__)

HEADERS = {"Content-type": "application/x-www-form-urlencoded"}
STATE_MAP = {'on': 1, 'off': 0}


@app.route('/')
def health():

    return jsonify({'status': 'up', 'message': 'Service is healthy.'})


@app.route('/api/v1/accessories', methods=['GET'])
def list_accessories():
    accessories = [{
        'id': accessory_id,
        'name': accessory.name
    } for accessory_id, accessory in ACCESSORIES.items()]
    return jsonify({'accessories': accessories})


@app.route('/api/v1/accessories/<int:accessory_id>/status', methods=['GET'])
def get_state(accessory_id):
    if accessory_id not in ACCESSORIES:
        abort(404)

    accessory = ACCESSORIES.get(accessory_id)
    return str(accessory.get_state())


@app.route('/api/v1/accessories/<int:accessory_id>/status', methods=['POST'])
def set_state(accessory_id):
    if accessory_id not in ACCESSORIES:
        abort(404)
    if not request.json:
        abort(400)
    raw_state = request.json.get('value')
    state = STATE_MAP.get(raw_state)
    accessory = ACCESSORIES.get(accessory_id)
    success = accessory.set_state(state)
    if success:
        return jsonify({'id': accessory_id, 'new_state': state})
    else:
        abort(400)
