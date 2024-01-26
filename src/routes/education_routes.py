from flask import Blueprint
from controllers.education_controller import get_educations, get_education, create_education, update_education, delete_education

education_routes = Blueprint('education_routes', __name__)

@education_routes.route('/educations', methods=['GET'])
def get_all_educations():
    return get_educations()

@education_routes.route('/education/<int:education_id>', methods=['GET'])
def get_single_education(education_id):
    return get_education(education_id)

@education_routes.route('/education', methods=['POST'])
def create_new_education():
    return create_education()

@education_routes.route('/education/<int:education_id>', methods=['PUT'])
def update_existing_education(education_id):
    return update_education(education_id)

@education_routes.route('/education/<int:education_id>', methods=['DELETE'])
def delete_existing_education(education_id):
    return delete_education(education_id)