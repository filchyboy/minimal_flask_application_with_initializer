'''
Base code for application
'''
# import flask module
from flask import Flask


def create_app():
# initiate application
    app = Flask(__name__)
    
    @app.route('/')
    def root():
        return('Hello world from within an initialized application. Repo <a href="https://github.com/filchyboy/minimal_flask_application_with_initializer">here</a>.')
    return app