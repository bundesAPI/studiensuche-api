# flake8: noqa

"""
    Arbeitsagentur Studiensuche API

    Eine der größten Datenbanken für Studienangebote in Deutschland durchsuchen.   Die Authentifizierung funktioniert über eine clientId:  **clientId:** infosysbub-studisu  Die clientId muss bei folgenden GET-requests an https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote  als Header-Parameter 'X-API-Key' zu übergeben.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


__version__ = "0.1.0"

# import ApiClient
from deutschland.studiensuche.api_client import ApiClient

# import Configuration
from deutschland.studiensuche.configuration import Configuration

# import exceptions
from deutschland.studiensuche.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)
