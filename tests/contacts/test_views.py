from http import HTTPStatus

from django.urls import reverse
from django.contrib.auth.models import User, Permission
import pytest


def test_contacts_thanks(client):
    # Given
    name = "Jhon"

    # Then
    response = client.get(f"/contacts/thanks/{name}")

    # When
    assert response.status_code == HTTPStatus.OK
    assert response.content.decode() == f"Obrigado {name}!"


def test_contact_create_with_unanuthenticated_user(client):
    # Given
    url = f'{reverse("accounts:login")}?next={reverse("contacts:create")}'
    # Then
    response = client.get(reverse("contacts:create"))

    # When
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == url


@pytest.mark.django_db
def test_contact_create_success(client, django_user_model):
    # Given
    data = {'subject': 'sasd@gmail.com',
            'menssage': "Hello World!!!",
            "sender": "sender@gmail.com",
            "cc_myself": True}
    user = django_user_model.objects.create_user(username='jhon', email='jhon@testmail.com', password="P@lavra123")
    permission = Permission.objects.get(codename="add_contact")
    user.user_permissions.add(permission)
    # Then
    client.force_login(user)
    response = client.post(reverse("contacts:create"), data)

    # When
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse("contacts:thanks", args=(data["subject"],))
