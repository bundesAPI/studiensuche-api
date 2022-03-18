"""
    Arbeitsagentur Studiensuche API

    Eine der größten Datenbanken für Studienangebote in Deutschland durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** 5aee2cfe-1709-48a9-951d-eb48f8f73a74  **ClientSecret:** 3309a57a-9214-40db-9abe-28b1bb30c08c  **Achtung**: der generierte Token muss bei folgenden GET-requests an https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote im header als 'OAuthAccessToken' inkludiert werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.studiensuche.model.response_studienangebot_abschlussgrad import (
    ResponseStudienangebotAbschlussgrad,
)
from deutschland.studiensuche.model.response_studienangebot_hochschulart import (
    ResponseStudienangebotHochschulart,
)
from deutschland.studiensuche.model.response_studienangebot_region import (
    ResponseStudienangebotRegion,
)
from deutschland.studiensuche.model.response_studienangebot_studienanbieter import (
    ResponseStudienangebotStudienanbieter,
)
from deutschland.studiensuche.model.response_studienangebot_studienform import (
    ResponseStudienangebotStudienform,
)
from deutschland.studiensuche.model.response_studienangebot_studienmodelle import (
    ResponseStudienangebotStudienmodelle,
)
from deutschland.studiensuche.model.response_studienangebot_studienort import (
    ResponseStudienangebotStudienort,
)
from deutschland.studiensuche.model.response_studienangebot_studientyp import (
    ResponseStudienangebotStudientyp,
)

from deutschland import studiensuche

globals()["ResponseStudienangebotAbschlussgrad"] = ResponseStudienangebotAbschlussgrad
globals()["ResponseStudienangebotHochschulart"] = ResponseStudienangebotHochschulart
globals()["ResponseStudienangebotRegion"] = ResponseStudienangebotRegion
globals()[
    "ResponseStudienangebotStudienanbieter"
] = ResponseStudienangebotStudienanbieter
globals()["ResponseStudienangebotStudienform"] = ResponseStudienangebotStudienform
globals()["ResponseStudienangebotStudienmodelle"] = ResponseStudienangebotStudienmodelle
globals()["ResponseStudienangebotStudienort"] = ResponseStudienangebotStudienort
globals()["ResponseStudienangebotStudientyp"] = ResponseStudienangebotStudientyp
from deutschland.studiensuche.model.response_studienangebot import (
    ResponseStudienangebot,
)


class TestResponseStudienangebot(unittest.TestCase):
    """ResponseStudienangebot unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseStudienangebot(self):
        """Test ResponseStudienangebot"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseStudienangebot()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
