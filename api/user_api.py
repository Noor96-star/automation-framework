from api.api_client import APIClient

class UserAPI:

    def __init__(self):
        self.client = APIClient()
        self.base_url = "https://reqres.in/api"

    def get_users(self):
        return self.client.get(f"{self.base_url}/users?page=2")

    def create_user(self, name, job):
        payload = {
            "name": name,
            "job": job
        }
        return self.client.post(f"{self.base_url}/users", payload=payload)
