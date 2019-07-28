# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "synprov"
VERSION = "0.4.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.0.0",
    "swagger-ui-bundle==0.0.2",
    "python_dateutil==2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="Provenance Service",
    author_email="",
    url="",
    keywords=["OpenAPI", "Provenance Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['synprov=synprov.__main__:main']},
    long_description="""\
    &lt;h1&gt;Platform Repository Service&lt;/h1&gt;&lt;p&gt;Sage Bionetworks Platform&lt;/p&gt;
    """
)

