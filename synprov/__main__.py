#!/usr/bin/env python3

import connexion

from synprov import config


def main():
    app = config.connex_app
    app.add_api('openapi.yaml', arguments={'title': 'Provenance Service'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
