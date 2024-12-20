import pytest

from ckan_client_tacc.models.portalx.user import PortalXUser, Response


def test_tacc_user_creation():
    user = PortalXUser.from_dict(
        data={
            "id": "123",
            "username": "testuser",
            "role": "user",
            "firstName": "Test",
            "lastName": "User",
            "email": "test@example.com",
        }
    )

    assert user.id == "123"
    assert user.username == "testuser"
    assert user.role == "user"
    assert user.firstName == "Test"
    assert user.lastName == "User"
    assert user.email == "test@example.com"


def test_response_from_response():
    mock_response = {
        "response": [
            {
                "id": "123",
                "username": "user1",
                "role": "admin",
                "firstName": "John",
                "lastName": "Doe",
                "email": "john@example.com",
            },
            {
                "id": "456",
                "username": "user2",
                "role": "user",
                "firstName": "Jane",
                "lastName": "Smith",
                "email": "jane@example.com",
            },
        ]
    }

    response = Response.from_response(mock_response)

    assert len(response.users) == 2

    # Check first user
    assert response.users[0].id == "123"
    assert response.users[0].username == "user1"
    assert response.users[0].role == "admin"
    assert response.users[0].firstName == "John"
    assert response.users[0].last_name == "Doe"
    assert response.users[0].email == "john@example.com"

    # Check second user
    assert response.users[1].id == "456"
    assert response.users[1].username == "user2"
    assert response.users[1].role == "user"
    assert response.users[1].firstName == "Jane"
    assert response.users[1].last_name == "Smith"
    assert response.users[1].email == "jane@example.com"


def test_response_from_response_empty():
    mock_response = {"response": []}
    response = Response.from_response(mock_response)
    assert len(response.users) == 0


def test_response_from_response_invalid_data():
    mock_response = {"response": [{"invalid": "data"}]}

    with pytest.raises(KeyError):
        Response.from_response(mock_response)
