#!/usr/bin/env python3

import connexion

from flask_graphql import GraphQLView

from synprov import config
from synprov.database import init_db
from synprov.schema import schema


def main():
    app = config.connex_app
    app.add_api('openapi.yaml', arguments={'title': 'Provenance Service'})

    default_query = '''
    {
      allActivities {
        edges {
          node {
            id,
            activityId,
            name,
            description,
            used {
              edges {
                node {
                  id,
                  targetId,
                  targetVersionNumber
                }
              }
            },
            generated {
              edges {
                node {
                  id,
                  targetId,
                  targetVersionNumber
                }
              }
            },
            agents {
              edges {
                node{
                  id,
                  agentId
                }
              }
            }
          }
        }
      }
    }'''.strip()

    app.app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', 
                                      schema=schema, 
                                      graphiql=True)
    )

    init_db()
    app.run(port=8080)

if __name__ == '__main__':
    main()
