#!/usr/bin/env python3

import connexion

from openapi_server import config


def main():
    app = config.connex_app
    app.add_api('openapi.yaml', arguments={'title': 'Platform Repository Service'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
