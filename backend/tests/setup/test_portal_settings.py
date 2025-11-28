"""Portal settings tests"""

from plone import api

import pytest


class TestPortalSettings:
    """Test portal settings"""

    @pytest.mark.parametrize(
        "key,expected",
        [
            ["plone.site_title", "Intranet do TRE-PI"],
            ["plone.email_from_name", "No Reply"],
            ["plone.smtp_host", "10.1.1.2"],
            ["plone.smtp_port", 25],
        ],
    )
    def test_portal_title(self, portal, key: str, expected: str):
        value = api.portal.get_registry_record(key)
        assert value == expected, f"Expected {expected}, but got {value} for key {key}"
