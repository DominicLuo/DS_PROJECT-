from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    from .config import Config
    app.config.from_object(Config)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = '/localhost:3307/mysql.3200-mysql-db'
    db.init_app(app)


    from .blueprints.user_routes import user_blueprint
    from .blueprints.conference_routes import conference_blueprint
    from .blueprints.gyms_routes import gyms_blueprint
    from .blueprints.gym_projects_routes import gym_projects_blueprint
    from .blueprints.user_level_routes import user_level_blueprint
    from .blueprints.product_orders_routes import product_orders_blueprint
    from .blueprints.products_routes import products_blueprint
    from .blueprints.foods_routes import foods_blueprint
    from .blueprints.diets_routes import diets_blueprint
    from .blueprints.food_order_routes import food_order_blueprint
    from .blueprints.suppliers_routes import suppliers_blueprint
    app.register_blueprint(suppliers_blueprint)
    app.register_blueprint(foods_blueprint)
    app.register_blueprint(diets_blueprint)
    app.register_blueprint(nutrition_logs_blueprint)
    app.register_blueprint(foods_diet_blueprint)
    app.register_blueprint(food_order_blueprint)
    app.register_blueprint(user_level_blueprint)
    app.register_blueprint(product_orders_blueprint)
    app.register_blueprint(products_blueprint)
    app.register_blueprint(gyms_blueprint)
    app.register_blueprint(gym_projects_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(conference_blueprint)

    return app
