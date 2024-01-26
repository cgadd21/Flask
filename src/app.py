from flask import Flask
from routes.education_routes import education_routes
from routes.experience_routes import experience_routes
from routes.project_routes import project_routes
from routes.skill_routes import skill_routes
from routes.volunteer_routes import volunteer_routes

app = Flask(__name__)

app.register_blueprint(education_routes)
app.register_blueprint(experience_routes)
app.register_blueprint(project_routes)
app.register_blueprint(skill_routes)
app.register_blueprint(volunteer_routes)

if __name__ == '__main__':
    app.run(debug=True)
