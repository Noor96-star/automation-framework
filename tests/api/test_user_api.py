from api.user_api import UserAPI

def test_get_users():
    api = UserAPI()
    response = api.get_users()

    print(response.text)   # debug

    assert response.status_code == 200
    assert "page" in response.text   # safer check


def test_create_user():
    api = UserAPI()
    response = api.create_user("john", "tester")

    print(response.text)

    assert response.status_code in [200, 201]
