from flask import Blueprint
from controllers.volunteer_controller import get_volunteers, get_volunteer, create_volunteer, update_volunteer, delete_volunteer

volunteer_routes = Blueprint('volunteer_routes', __name__)

@volunteer_routes.route('/volunteers', methods=['GET'])
def get_all_volunteers():
    return get_volunteers()

@volunteer_routes.route('/volunteer/<int:volunteer_id>', methods=['GET'])
def get_single_volunteer(volunteer_id):
    return get_volunteer(volunteer_id)

@volunteer_routes.route('/volunteer', methods=['POST'])
def create_new_volunteer():
    return create_volunteer()

@volunteer_routes.route('/volunteer/<int:volunteer_id>', methods=['PUT'])
def update_existing_volunteer(volunteer_id):
    return update_volunteer(volunteer_id)

@volunteer_routes.route('/volunteer/<int:volunteer_id>', methods=['DELETE'])
def delete_existing_volunteer(volunteer_id):
    return delete_volunteer(volunteer_id)