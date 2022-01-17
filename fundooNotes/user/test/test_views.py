import pytest
from rest_framework.reverse import reverse


pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestUser:
    def test_user_registration(self, client):
        #test case create their own database to test the views
        url = reverse("user_registration")
        user = {
            "username": "sunanda",
            "password": "root",
            "age": 24,
            "email": "ssunanda02@gmail.com",
            "first_name": "sunanda",
            "last_name": "shil",
            "is_verified": 0
        }
        response = client.post(url, user)
        assert response.status_code == 201
