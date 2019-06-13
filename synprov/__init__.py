import connexion

from healthcheck import HealthCheck

from synprov import config

def neo4j_available():
    if config.neomod.test_connection():
        return True, "neo4j ok"
    else:
        return False, "neo4j connection not found"


def create_app():
    app = config.connex_app
    app.add_api('openapi.yaml', arguments={'title': 'Provenance Service'})
    # wrap the flask app and give a heathcheck url
    health = HealthCheck(app, "/healthcheck")
    health.add_check(neo4j_available)

    return app








