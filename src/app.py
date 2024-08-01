from flask import Flask, render_template
from flask_restx import Api
from api.carNS import car_ns
from .database import db


def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auction.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
            db.create_all()

    api.add_namespace(car_ns)

    @app.route('/admin')
    def hello():
        return render_template('admin.html')

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=7890)
