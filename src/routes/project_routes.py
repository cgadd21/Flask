from flask import Blueprint
from controllers.project_controller import get_projects, get_project, create_project, update_project, delete_project

project_routes = Blueprint('project_routes', __name__)

@project_routes.route('/projects', methods=['GET'])
def get_all_projects():
    return get_projects()

@project_routes.route('/project/<int:project_id>', methods=['GET'])
def get_single_project(project_id):
    return get_project(project_id)

@project_routes.route('/project', methods=['POST'])
def create_new_project():
    return create_project()

@project_routes.route('/project/<int:project_id>', methods=['PUT'])
def update_existing_project(project_id):
    return update_project(project_id)

@project_routes.route('/project/<int:project_id>', methods=['DELETE'])
def delete_existing_project(project_id):
    return delete_project(project_id)