import pytest

from ckan_client_tacc.models.ckan.user import CkanUser
from ckan_client_tacc.models.tacc.user import TaccUser
from ckan_client_tacc.models.UserMapper import ORG_ALLOCATION_MAPPING, UserMapper


class TestUserMapper:
    def test_map_to_ckan_user(self):
        # Arrange
        tacc_user = TaccUser(
            id="123",
            username="testuser",
            first_name="Test",
            last_name="User",
            email="test@example.com",
            role="admin",
        )

        # Act
        ckan_user = UserMapper.map_to_ckan_user(tacc_user)

        # Assert
        assert isinstance(ckan_user, CkanUser)
        assert ckan_user.id == "123"
        assert ckan_user.name == "testuser"
        assert ckan_user.fullname == "Test User"
        assert ckan_user.sysadmin is True
        assert ckan_user.state == "active"

    def test_map_to_ckan_user_inactive(self):
        # Test inactive user mapping
        tacc_user = TaccUser(
            id="456",
            username="inactiveuser",
            first_name="Inactive",
            last_name="User",
            email="inactive@example.com",
            role="inactive",
        )

        ckan_user = UserMapper.map_to_ckan_user(tacc_user)
        assert ckan_user.state == "inactive"

    def test_map_from_ckan_user(self):
        # Arrange
        ckan_user = CkanUser(
            id="789",
            name="ckanuser",
            fullname="CKAN User",
            email_hash="ckan@example.com",
            sysadmin=True,
            created="2024-01-01",
            about=None,
            activity_streams_email_notifications=False,
            state="active",
            image_url=None,
            display_name="ckanuser",
            number_created_packages=0,
            image_display_url=None,
        )

        # Act
        tacc_user = UserMapper.map_from_ckan_user(ckan_user)

        # Assert
        assert isinstance(tacc_user, TaccUser)
        assert tacc_user.id == "789"
        assert tacc_user.username == "ckanuser"
        assert tacc_user.first_name == "CKAN"
        assert tacc_user.last_name == "User"
        assert tacc_user.role == "admin"

    def test_map_organization(self):
        # Test valid organization mapping
        assert UserMapper.map_organization("planet-texas-2050") == "BCS2411"
        assert UserMapper.map_organization("SETx-UIFL") == "CA23001"
        assert UserMapper.map_organization("dynamo") == "BCS24008"

    def test_map_organization_invalid(self):
        # Test invalid organization mapping
        with pytest.raises(ValueError) as exc_info:
            UserMapper.map_organization("invalid-org")
        assert "Organization invalid-org not found in mapping" in str(exc_info.value)
