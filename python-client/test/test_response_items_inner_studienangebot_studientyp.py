"""
    Arbeitsagentur Studiensuche API

    Eine der größten Datenbanken für Studienangebote in Deutschland durchsuchen.   Die Authentifizierung funktioniert über eine clientId:  **clientId:** infosysbub-studisu  Die clientId muss bei folgenden GET-requests an https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote  als Header-Parameter 'X-API-Key' zu übergeben.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

from deutschland.studiensuche.model.response_items_inner_studienangebot_studientyp import (
    ResponseItemsInnerStudienangebotStudientyp,
)

from deutschland import studiensuche


class TestResponseItemsInnerStudienangebotStudientyp(unittest.TestCase):
    """ResponseItemsInnerStudienangebotStudientyp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseItemsInnerStudienangebotStudientyp(self):
        """Test ResponseItemsInnerStudienangebotStudientyp"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseItemsInnerStudienangebotStudientyp()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
