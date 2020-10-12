import json
import uuid

import requests
from django.conf import settings
from django.db import transaction
from rest_framework.views import Response, status

from apps.users.models import User

# TODO: Add Auth0 Error Handling
def fetch_auth0_token():
    url = f"{settings.AUTH_URL}/oauth/token"
    payload = f"grant_type=client_credentials&client_id={settings.AUTH_CLIENT_ID}&client_secret={settings.AUTH_CLIENT_SECRET}&audience={settings.AUTH_AUDIENCE}&account.namespace%7D%2Fapi%2Fv2%2F"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    res = requests.post(url, headers=headers, data=payload)
    data = json.loads(res.text)
    return data["access_token"]


def generate_password_recovery(user_id, token):
    try:
        url = f"{settings.AUTH_URL}/api/v2/tickets/password-change"

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token,
        }

        payload = {
            "mark_email_as_verified": True,
            "user_id": user_id,
            "result_url": "http://localhost:3000/",
        }
        res = requests.post(url, headers=headers, data=json.dumps(payload))
        f_res = json.loads(res.text)

        return f_res.get("ticket")
    except Exception as e:
        raise Exception(str(e))


def create_password_recovery(wat_id, email):
    # TODO: Handle Auth0 Errors
    try:
        with transaction.atomic():
            if User.objects.filter(email=email).exists():
                raise Exception("User with given email already exists")

            auth_token = fetch_auth0_token()

            user_created = User.objects.create(wat_id=wat_id, email=email)

            user_info = {
                "connection": "Username-Password-Authentication",
                "email": email,
                "password": str(uuid.uuid4),
                "email_verified": False,
                "verify_email": False,
            }

            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + auth_token,
            }

            url = f"{settings.AUTH_URL}/api/v2/users"
            res = requests.post(url, headers=headers, data=json.dumps(user_info))

            f_res = json.loads(res.text)

            user_created.auth_id = f_res.get("user_id")
            user_created.save()

            password_recovery_link = generate_password_recovery(
                f_res.get("user_id"), auth_token
            )

            return password_recovery_link

    except Exception as e:
        raise Exception(str(e))
