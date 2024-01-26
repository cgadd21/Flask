from flask import jsonify, request
from config import db, cursor

def get_educations():
    try:
        cursor.execute("SELECT * FROM education")
        educations = cursor.fetchall()
        education_list = [{'educationId': edu[0], 'institutionName': edu[1], 'degree': edu[2], 'graduationYear': edu[3]} for edu in educations]
        return jsonify(education_list)
    except Exception as e:
        return jsonify({"message": f"Error fetching educations: {str(e)}"}), 500

def get_education(education_id):
    try:
        cursor.execute("SELECT * FROM education WHERE educationId = %s", (education_id,))
        education = cursor.fetchone()
        if education:
            return jsonify({'educationId': education[0], 'institutionName': education[1], 'degree': education[2], 'graduationYear': education[3]})
        else:
            return jsonify({"message": "Education not found"}), 404
    except Exception as e:
        return jsonify({"message": f"Error fetching education: {str(e)}"}), 500

def create_education():
    data = request.get_json()
    institution_name = data.get('institutionName')
    degree = data.get('degree')
    graduation_year = data.get('graduationYear')
    
    if institution_name and degree and graduation_year:
        try:
            query = "INSERT INTO education (institutionName, degree, graduationYear) VALUES (%s, %s, %s)"
            cursor.execute(query, (institution_name, degree, graduation_year))
            db.commit()
            return jsonify({"message": "Education created successfully"}), 201
        except Exception as e:
            return jsonify({"message": f"Error creating education: {str(e)}"}), 500
    else:
        return jsonify({"message": "Missing required data"}), 400

def update_education(education_id):
    data = request.get_json()
    institution_name = data.get('institutionName')
    degree = data.get('degree')
    graduation_year = data.get('graduationYear')

    if institution_name and degree and graduation_year:
        try:
            query = "UPDATE education SET institutionName = %s, degree = %s, graduationYear = %s WHERE educationId = %s"
            cursor.execute(query, (institution_name, degree, graduation_year, education_id))
            db.commit()
            return jsonify({"message": "Education updated successfully"})
        except Exception as e:
            return jsonify({"message": f"Error updating education: {str(e)}"}), 500
    else:
        return jsonify({"message": "Missing required data"}), 400

def delete_education(education_id):
    try:
        query = "DELETE FROM education WHERE educationId = %s"
        cursor.execute(query, (education_id,))
        db.commit()
        return jsonify({"message": "Education deleted successfully"})
    except Exception as e:
        return jsonify({"message": f"Error deleting education: {str(e)}"}), 500