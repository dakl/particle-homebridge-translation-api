import logging

from flask import abort, jsonify, request

from app.accessories import ACCESSORIES
from app.setup import app

logger = logging.getLogger(__name__)

HEADERS = {"Content-type": "application/x-www-form-urlencoded"}
ALLOWED_ACTIONS = {'on': 'HIGH', 'off': 'LOW'}


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
    response = accessory.get_status()
    return str(response.get('status'))


@app.route('/api/v1/accessories/<int:accessory_id>/status', methods=['POST'])
def set_state(accessory_id):
    if accessory_id not in ACCESSORIES:
        abort(404)
    state = int(request.json.get('value'))
    accessory = ACCESSORIES.get(accessory_id)
    success = accessory.set_state(state)
    if success:
        return jsonify({
            'id': accessory_id,
            'new_state': state
        })
    else:
        abort(400)
