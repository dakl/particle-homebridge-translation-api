import logging

from requests import post

from app.config import Config as config
from app.setup import app
from flask import abort, jsonify
from app.accessories import ACCESSORIES
logger = logging.getLogger(__name__)

HEADERS = {"Content-type": "application/x-www-form-urlencoded"}
ALLOWED_ACTIONS = {'on': 'HIGH', 'off': 'LOW'}


@app.route('/')
def health():
    return jsonify({'status': 'up', 'message': 'Service is healthy.'})


@app.route('/relays', methods=['GET'])
def list_relays():
    relays = [{
        'id': relay_id,
        'name': relay.name
    } for relay_id, relay in ACCESSORIES.items()]
    return jsonify({'relays': relays})


@app.route('/relay/<int:relay_id>', methods=['GET'])
def relay(relay_id):
    if relay_id not in ACCESSORIES:
        abort(404)

    relay = ACCESSORIES.get(relay_id)
    response = relay.get_status()
    response['id'] = relay_id
    return jsonify({'id': relay_id, 'status': response.get('status')})


@app.route('/relay/<int:relay_id>/<action>', methods=['POST'])
def set_relay(relay_id, action):
    if relay_id not in ACCESSORIES:
        abort(404)
    if action not in ALLOWED_ACTIONS.keys():
        abort(400)

    relay = ACCESSORIES.get(relay_id)
    response = relay.set_state(action)

    return jsonify({
        'id': relay_id,
        'action': action,
        'status': response.get('status')
    })
