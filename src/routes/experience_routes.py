from flask import Blueprint
from controllers.experience_controller import get_experiences, get_experience, create_experience, update_experience, delete_experience

experience_routes = Blueprint('experience_routes', __name__)

@experience_routes.route('/experiences', methods=['GET'])
def get_all_experiences():
    return get_experiences()

@experience_routes.route('/experience/<int:experience_id>', methods=['GET'])
def get_single_experience(experience_id):
    return get_experience(experience_id)

@experience_routes.route('/experience', methods=['POST'])
def create_new_experience():
    return create_experience()

@experience_routes.route('/experience/<int:experience_id>', methods=['PUT'])
def update_existing_experience(experience_id):
    return update_experience(experience_id)

@experience_routes.route('/experience/<int:experience_id>', methods=['DELETE'])
def delete_existing_experience(experience_id):
    return delete_experience(experience_id)