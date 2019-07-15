import logging
import connexion

from healthcheck import HealthCheck

from synprov.config import connex_app
from synprov.config import neo4j_connection


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def neo4j_available():
    try:
        logger.info("Checking connection at {}"
                     .format(neo4j_connection.database.uri))
        neo4j_connection.run('MATCH () RETURN 1 LIMIT 1')
        return True, "neo4j ok"
    except AttributeError:
        return False, "neo4j connection not found"


def create_app():
    app = connex_app
    app.add_api('openapi.yaml', arguments={'title': 'Provenance Service'})
    # wrap the flask app and give a heathcheck url
    health = HealthCheck(app, "/healthcheck")
    health.add_check(neo4j_available)

    return app








