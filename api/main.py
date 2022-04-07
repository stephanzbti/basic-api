from flask import Flask
from src.config.config import *
from src.routes.routes import Routes
import logging


class Service():
    app = None

    def __init__(self, app=None):
        super()

        if app != None:
            self.app = app
        else:
            self.create_app()

    # Create the basic app
    def create_app(self):
        logging.info(f'Starting app in {ENVIRONMENT} environment')
        app = Flask(__name__)
        self.app = app

        self.load_routes()

        return self.app

    # Function to load routes (TO DO: Migrate it to other class)
    def load_routes(self):
        self.app.add_url_rule('/', 'home', Routes.root)
        self.app.add_url_rule('/__healthcheck__',
                              'healthcheck', Routes.healthcheck)

    # Flask Start
    def run(self):
        logging.info(f'Starting service on host {HOST_BINDING}:{HOST_PORT}')
        self.app.run(host=HOST_BINDING, port=HOST_PORT)


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s', level=LOG_LEVEL)

    app = Service()

    app.run()
