from flask import jsonify, request
from config import db, cursor

def get_volunteers():
    try:
        cursor.execute("SELECT * FROM volunteer")
        volunteers = cursor.fetchall()
        volunteer_list = [{'volunteerId': vol[0], 'jobTitle': vol[1], 'companyName': vol[2], 'description': vol[3], 'link': vol[4]} for vol in volunteers]
        return jsonify(volunteer_list)
    except Exception as e:
        return jsonify({"message": f"Error fetching volunteers: {str(e)}"}), 500

def get_volunteer(volunteer_id):
    try:
        cursor.execute("SELECT * FROM volunteer WHERE volunteerId = %s", (volunteer_id,))
        volunteer = cursor.fetchone()
        if volunteer:
            return jsonify({'volunteerId': volunteer[0], 'jobTitle': volunteer[1], 'companyName': volunteer[2], 'description': volunteer[3], 'link': volunteer[4]})
        else:
            return jsonify({"message": "Volunteer not found"}), 404
    except Exception as e:
        return jsonify({"message": f"Error fetching volunteer: {str(e)}"}), 500

def create_volunteer():
    data = request.get_json()
    job_title = data.get('jobTitle')
    company_name = data.get('companyName')
    description = data.get('description')
    link = data.get('link')

    if job_title and company_name and description:
        try:
            query = "INSERT INTO volunteer (jobTitle, companyName, description, link) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (job_title, company_name, description, link))
            db.commit()
            return jsonify({"message": "Volunteer created successfully"}), 201
        except Exception as e:
            return jsonify({"message": f"Error creating volunteer: {str(e)}"}), 500
    else:
        return jsonify({"message": "Missing required data"}), 400

def update_volunteer(volunteer_id):
    data = request.get_json()
    job_title = data.get('jobTitle')
    company_name = data.get('companyName')
    description = data.get('description')
    link = data.get('link')

    if job_title and company_name and description:
        try:
            query = "UPDATE volunteer SET jobTitle = %s, companyName = %s, description = %s, link = %s WHERE volunteerId = %s"
            cursor.execute(query, (job_title, company_name, description, link, volunteer_id))
            db.commit()
            return jsonify({"message": "Volunteer updated successfully"})
        except Exception as e:
            return jsonify({"message": f"Error updating volunteer: {str(e)}"}), 500
    else:
        return jsonify({"message": "Missing required data"}), 400

def delete_volunteer(volunteer_id):
    try:
        query = "DELETE FROM volunteer WHERE volunteerId = %s"
        cursor.execute(query, (volunteer_id,))
        db.commit()
        return jsonify({"message": "Volunteer deleted successfully"})
    except Exception as e:
        return jsonify({"message": f"Error deleting volunteer: {str(e)}"}), 500