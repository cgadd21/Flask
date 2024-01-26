from flask import jsonify, request
from config import db, cursor

def get_projects():
    try:
        cursor.execute("SELECT * FROM project")
        projects = cursor.fetchall()
        project_list = [{'projectId': project[0], 'projectName': project[1], 'projectLink': project[2], 'projectDescription': project[3]} for project in projects]
        return jsonify(project_list)
    except Exception as e:
        return jsonify({"message": f"Error fetching projects: {str(e)}"}), 500

def get_project(project_id):
    try:
        cursor.execute("SELECT * FROM project WHERE projectId = %s", (project_id,))
        project = cursor.fetchone()
        if project:
            return jsonify({'projectId': project[0], 'projectName': project[1], 'projectLink': project[2], 'projectDescription': project[3]})
        else:
            return jsonify({"message": "Project not found"}), 404
    except Exception as e:
        return jsonify({"message": f"Error fetching project: {str(e)}"}), 500

def create_project():
    data = request.get_json()
    project_name = data.get('projectName')
    project_link = data.get('projectLink')
    project_description = data.get('projectDescription')
    
    if project_name:
        try:
            query = "INSERT INTO project (projectName, projectLink, projectDescription) VALUES (%s, %s, %s)"
            cursor.execute(query, (project_name, project_link, project_description))
            db.commit()
            return jsonify({"message": "Project created successfully"}), 201
        except Exception as e:
            return jsonify({"message": f"Error creating project: {str(e)}"}), 500
    else:
        return jsonify({"message": "Missing required data"}), 400

def update_project(project_id):
    data = request.get_json()
    project_name = data.get('projectName')
    project_link = data.get('projectLink')
    project_description = data.get('projectDescription')

    if project_name:
        try:
            query = "UPDATE project SET projectName = %s, projectLink = %s, projectDescription = %s WHERE projectId = %s"
            cursor.execute(query, (project_name, project_link, project_description, project_id))
            db.commit()
            return jsonify({"message": "Project updated successfully"})
        except Exception as e:
            return jsonify({"message": f"Error updating project: {str(e)}"}), 500
    else:
        return jsonify({"message": "Missing required data"}), 400

def delete_project(project_id):
    try:
        query = "DELETE FROM project WHERE projectId = %s"
        cursor.execute(query, (project_id,))
        db.commit()
        return jsonify({"message": "Project deleted successfully"})
    except Exception as e:
        return jsonify({"message": f"Error deleting project: {str(e)}"}), 500