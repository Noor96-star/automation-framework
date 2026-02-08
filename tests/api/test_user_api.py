import pytest
from api.user_api import UserAPI

@pytest.mark.skip(reason="Skipping API in CI - external API blocked")
def test_get_users():
    api = UserAPI()
    response = api.get_users()

    assert response.status_code == 200


@pytest.mark.skip(reason="Skipping API in CI - external API blocked")
def test_create_user():
    api = UserAPI()
    response = api.create_user("john", "tester")

    assert response.status_code in [200, 201]
