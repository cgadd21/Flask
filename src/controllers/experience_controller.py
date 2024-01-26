from flask import jsonify, request
from config import db, cursor

def get_experiences():
    try:
        cursor.execute("SELECT * FROM experience")
        experiences = cursor.fetchall()
        experience_list = [{'experienceId': exp[0], 'jobTitle': exp[1], 'companyName': exp[2], 'employmentType': exp[3],
                            'startDate': exp[4], 'endDate': exp[5], 'description': exp[6], 'link': exp[7]} for exp in experiences]
        return jsonify(experience_list)
    except Exception as e:
        return jsonify({"message": f"Error fetching experiences: {str(e)}"}), 500

def get_experience(experience_id):
    try:
        cursor.execute("SELECT * FROM experience WHERE experienceId = %s", (experience_id,))
        experience = cursor.fetchone()
        if experience:
            return jsonify({'experienceId': experience[0], 'jobTitle': experience[1], 'companyName': experience[2],
                            'employmentType': experience[3], 'startDate': experience[4], 'endDate': experience[5],
                            'description': experience[6], 'link': experience[7]})
        else:
            return jsonify({"message": "Experience not found"}), 404
    except Exception as e:
        return jsonify({"message": f"Error fetching experience: {str(e)}"}), 500

def create_experience():
    data = request.get_json()
    job_title = data.get('jobTitle')
    company_name = data.get('companyName')
    employment_type = data.get('employmentType')
    start_date = data.get('startDate')
    end_date = data.get('endDate')
    description = data.get('description')
    link = data.get('link')

    if job_title and company_name and employment_type and start_date and end_date and description:
        try:
            query = "INSERT INTO experience (jobTitle, companyName, employmentType, startDate, endDate, description, link) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (job_title, company_name, employment_type, start_date, end_date, description, link))
            db.commit()
            return jsonify({"message": "Experience created successfully"}), 201
        except Exception as e:
            return jsonify({"message": f"Error creating experience: {str(e)}"}), 500
    else:
        return jsonify({"message": "Missing required data"}), 400

def update_experience(experience_id):
    data = request.get_json()
    job_title = data.get('jobTitle')
    company_name = data.get('companyName')
    employment_type = data.get('employmentType')
    start_date = data.get('startDate')
    end_date = data.get('endDate')
    description = data.get('description')
    link = data.get('link')

    if job_title and company_name and employment_type and start_date and end_date and description:
        try:
            query = "UPDATE experience SET jobTitle = %s, companyName = %s, employmentType = %s, startDate = %s, endDate = %s, description = %s, link = %s WHERE experienceId = %s"
            cursor.execute(query, (job_title, company_name, employment_type, start_date, end_date, description, link, experience_id))
            db.commit()
            return jsonify({"message": "Experience updated successfully"})
        except Exception as e:
            return jsonify({"message": f"Error updating experience: {str(e)}"}), 500
    else:
        return jsonify({"message": "Missing required data"}), 400

def delete_experience(experience_id):
    try:
        query = "DELETE FROM experience WHERE experienceId = %s"
        cursor.execute(query, (experience_id,))
        db.commit()
        return jsonify({"message": "Experience deleted successfully"})
    except Exception as e:
        return jsonify({"message": f"Error deleting experience: {str(e)}"}), 500