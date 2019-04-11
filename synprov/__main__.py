#!/usr/bin/env python3

import connexion

from flask_graphql import GraphQLView
from graphene import Schema

from synprov import config
# from synprov.schema import Query


def main():
    app = config.connex_app
    app.add_api('openapi.yaml', arguments={'title': 'Provenance Service'})
    # app.app.add_url_rule(
    #     '/graphql',
    #     view_func=GraphQLView.as_view('graphql', 
    #                                   schema=Schema(query=Query), 
    #                                   graphiql=True)
    # )
    app.run(port=8080)


if __name__ == '__main__':
    main()
