from flask import jsonify, request
from config import db, cursor

def get_skills():
    try:
        cursor.execute("SELECT * FROM skill")
        skills = cursor.fetchall()
        skill_list = [{'skillId': skill[0], 'category': skill[1], 'skillName': skill[2]} for skill in skills]
        return jsonify(skill_list)
    except Exception as e:
        return jsonify({"message": f"Error fetching skills: {str(e)}"}), 500

def get_skill(skill_id):
    try:
        cursor.execute("SELECT * FROM skill WHERE skillId = %s", (skill_id,))
        skill = cursor.fetchone()
        if skill:
            return jsonify({'skillId': skill[0], 'category': skill[1], 'skillName': skill[2]})
        else:
            return jsonify({"message": "Skill not found"}), 404
    except Exception as e:
        return jsonify({"message": f"Error fetching skill: {str(e)}"}), 500

def create_skill():
    data = request.get_json()
    category = data.get('category')
    skill_name = data.get('skillName')
    
    if category and skill_name:
        try:
            query = "INSERT INTO skill (category, skillName) VALUES (%s, %s)"
            cursor.execute(query, (category, skill_name))
            db.commit()
            return jsonify({"message": "Skill created successfully"}), 201
        except Exception as e:
            return jsonify({"message": f"Error creating skill: {str(e)}"}), 500
    else:
        return jsonify({"message": "Missing required data"}), 400

def update_skill(skill_id):
    data = request.get_json()
    category = data.get('category')
    skill_name = data.get('skillName')

    if category and skill_name:
        try:
            query = "UPDATE skill SET category = %s, skillName = %s WHERE skillId = %s"
            cursor.execute(query, (category, skill_name, skill_id))
            db.commit()
            return jsonify({"message": "Skill updated successfully"})
        except Exception as e:
            return jsonify({"message": f"Error updating skill: {str(e)}"}), 500
    else:
        return jsonify({"message": "Missing required data"}), 400

def delete_skill(skill_id):
    try:
        query = "DELETE FROM skill WHERE skillId = %s"
        cursor.execute(query, (skill_id,))
        db.commit()
        return jsonify({"message": "Skill deleted successfully"})
    except Exception as e:
        return jsonify({"message": f"Error deleting skill: {str(e)}"}), 500