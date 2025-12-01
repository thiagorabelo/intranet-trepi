from AccessControl.users import nobody
from plone import api

import pytest


class TestPloneSite:
    def test_workflow_state(self, portal):
        """Verifica se o workflow está correto"""
        expected = "internal"
        value = api.content.get_state(portal)
        assert value == expected, f"Expected workflow is {expected}, got {value}"

    @pytest.mark.parametrize(
        "permission,expected",
        [
            ["Access contents information", False],
            ["Modify portal content", False],
            ["View", False],
        ],
    )
    def test_anonymous_permissions(self, portal, permission: str, expected: str):
        with api.env.adopt_user(user=nobody):
            user = api.user.get_current()
            has_permission = api.user.has_permission(permission, user=user, obj=portal)
            assert has_permission is expected, (
                f"Error: Permission {permission} to anounymous user: {has_permission}"
            )
