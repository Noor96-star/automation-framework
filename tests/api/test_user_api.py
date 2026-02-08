from api.user_api import UserAPI

def test_get_users():
    api = UserAPI()
    response = api.get_users()

    print(response.json())
    assert response.status_code == 200


def test_create_user():
    api = UserAPI()
    response = api.create_user("john", "tester")

    print(response.json())
    assert response.status_code == 201
