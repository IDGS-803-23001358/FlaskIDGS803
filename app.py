from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db
from flask_migrate import Migrate

from alumnos import alumnos
from maestros import maestros
from cursos import cursos
from inscripciones import inscripciones
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()
csrf = CSRFProtect(app)

app.register_blueprint(alumnos)
app.register_blueprint(maestros)
app.register_blueprint(cursos)
app.register_blueprint(inscripciones)


@app.route("/", methods=['GET','POST'])
def home():
    return render_template("home.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)

