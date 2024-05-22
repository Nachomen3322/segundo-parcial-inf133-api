from flask import Flask
from flask_jwt_extended import JWTManager
from controllers.user_controller import user_bp
from controllers.task_controller import task_bp
from flask_swagger_ui import get_swaggerui_blueprint
from database import db

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "tu_clave_secreta"
SWAGGET_URL = "/api/docs"

API_URL = "/static/swagger.json"
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGET_URL, API_URL, config={"app_name": "Libreia API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix = SWAGGET_URL)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db.init_app(app)

jwt = JWTManager(app)

app.register_blueprint(task_bp, url_prefix="/api")
app.register_blueprint(user_bp, url_prefix="/api")

with app.app_context():
    db.create_all()
    
if __name__ == "__main__":
    app.run(debug=True)