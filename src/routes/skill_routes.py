from flask import Blueprint
from controllers.skill_controller import get_skills, get_skill, create_skill, update_skill, delete_skill

skill_routes = Blueprint('skill_routes', __name__)

@skill_routes.route('/skills', methods=['GET'])
def get_all_skills():
    return get_skills()

@skill_routes.route('/skill/<int:skill_id>', methods=['GET'])
def get_single_skill(skill_id):
    return get_skill(skill_id)

@skill_routes.route('/skill', methods=['POST'])
def create_new_skill():
    return create_skill()

@skill_routes.route('/skill/<int:skill_id>', methods=['PUT'])
def update_existing_skill(skill_id):
    return update_skill(skill_id)

@skill_routes.route('/skill/<int:skill_id>', methods=['DELETE'])
def delete_existing_skill(skill_id):
    return delete_skill(skill_id)