#!/usr/bin/env python3

import connexion

from synprov import config
from synprov.graphdb import init_db


def main():
    app = config.connex_app
    app.add_api('openapi.yaml', arguments={'title': 'Provenance Service'})
    print("Running `init_db()`")

    init_db()
    app.run(host='localhost', port=8080, debug=True)

if __name__ == '__main__':
    main()
