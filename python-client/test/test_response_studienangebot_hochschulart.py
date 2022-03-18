"""
    Arbeitsagentur Studiensuche API

    Eine der größten Datenbanken für Studienangebote in Deutschland durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** 5aee2cfe-1709-48a9-951d-eb48f8f73a74  **ClientSecret:** 3309a57a-9214-40db-9abe-28b1bb30c08c  **Achtung**: der generierte Token muss bei folgenden GET-requests an https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote im header als 'OAuthAccessToken' inkludiert werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.studiensuche.model.response_studienangebot_hochschulart import (
    ResponseStudienangebotHochschulart,
)

from deutschland import studiensuche


class TestResponseStudienangebotHochschulart(unittest.TestCase):
    """ResponseStudienangebotHochschulart unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseStudienangebotHochschulart(self):
        """Test ResponseStudienangebotHochschulart"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseStudienangebotHochschulart()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
