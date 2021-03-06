from requests import post
from flask import Flask, render_template, request

from flask_graphql import GraphQLView
from flask_cors import CORS
from flask_json import FlaskJSON

from flask_mail import Mail
from config import config, Config
from helpers.database import db_session
from schema import schema
from healthcheck_schema import healthcheck_schema
from helpers.auth.authentication import Auth
from api.analytics.analytics_request import AnalyticsRequest

mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    FlaskJSON(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    mail.init_app(app)

    @app.route("/notifications", methods=["POST", "GET"])
    def redirect_notifications():
        post(Config.MRM_PUSH_URL + "/notifications",
             data=request.data, headers=request.headers)
        return 'OK'

    @app.route("/", methods=['GET'])
    def index():
        return render_template('index.html')

    app.add_url_rule(
        '/mrm',
        view_func=GraphQLView.as_view(
            'mrm',
            schema=schema,
            graphiql=True   # for having the GraphiQL interface
        )
    )
    app.add_url_rule(
        '/_healthcheck',
        view_func=GraphQLView.as_view(
            '_healthcheck',
            schema=healthcheck_schema,
            graphiql=True   # for healthchecks
        )
    )

    @app.route("/analytics", methods=['POST'])
    @Auth.user_roles('Admin', 'REST')
    def analytics_report():
        return AnalyticsRequest.validate_request(AnalyticsRequest)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
