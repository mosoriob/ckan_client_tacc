from ckan_client_tacc.models.ckan.user import CkanUser


def test_user_from_dict():
    user_dict = {
        "id": "7003d3c9-8596-45b4-9064-7194bd09b187",
        "name": "lafletch",
        "fullname": "Lydia",
        "created": "2024-12-16T19:54:51.036882",
        "about": None,
        "activity_streams_email_notifications": False,
        "sysadmin": False,
        "state": "active",
        "image_url": None,
        "display_name": "Lydia",
        "email_hash": "0ad932be14d60f084f1ad68c5a75bd2f",
        "number_created_packages": 0,
        "image_display_url": None,
        "apikey": None,
        "email": "lafletch@example.com",
    }

    user = CkanUser(**user_dict)

    assert user.id == "7003d3c9-8596-45b4-9064-7194bd09b187"
    assert user.name == "lafletch"
    assert user.fullname == "Lydia"
    assert user.created == "2024-12-16T19:54:51.036882"
    assert user.about is None
    assert user.activity_streams_email_notifications is False
    assert user.sysadmin is False
    assert user.state == "active"
    assert user.image_url is None
    assert user.display_name == "Lydia"
    assert user.email_hash == "0ad932be14d60f084f1ad68c5a75bd2f"
    assert user.number_created_packages == 0
    assert user.image_display_url is None
