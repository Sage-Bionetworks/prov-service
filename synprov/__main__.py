#!/usr/bin/env python3

import connexion

from synprov import create_app
from synprov.graphdb import init_db


def main():
    app = create_app()

    init_db()
    app.run(host='localhost', port=8080, debug=True)

if __name__ == '__main__':
    main()
