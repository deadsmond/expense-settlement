import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_group_api_create_and_fetch():
    user = User.objects.create_user(username="bob", password="pass456")
    client = APIClient()
    client.force_authenticate(user=user)

    # Create Group
    response = client.post("/api/groups/", {"name": "Work"}, format="json")
    assert response.status_code == 201
    group_id = response.data["id"]

    # Fetch Group
    response = client.get(f"/api/groups/{group_id}/")
    assert response.status_code == 200
    assert response.data["name"] == "Work"
