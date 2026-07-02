import jwt  # Install with `pip install pyjwt`
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.backends import default_backend
import base64
from datetime import datetime, timedelta, timezone
import requests

def load_private_key(cert_path, password=None):
    """
    Load the private key from a .pfx file.
    """
    try:
        with open(cert_path, "rb") as key_file:
            private_key, _, _ = pkcs12.load_key_and_certificates(
                key_file.read(), password=password, backend=default_backend()
            )
        return private_key
    except Exception as e:
        raise ValueError(f"Error loading private key: {e}")

def create_jwt_assertion(tenant_id, client_id, cert_private_key, thumbprint):
    """
    Create a JWT assertion for Azure AD token endpoint.
    """
    now = datetime.now(timezone.utc)
    exp_time = now + timedelta(minutes=10)

    # Convert thumbprint to Base64 format if not already encoded
    if not thumbprint.startswith("MI"):
        thumbprint_bytes = bytes.fromhex(thumbprint.replace(":", ""))
        thumbprint = base64.b64encode(thumbprint_bytes).decode("utf-8")

    token = {
        "aud": f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token",
        "iss": client_id,
        "sub": client_id,
        "jti": "random-jwt-id",
        "exp": int(exp_time.timestamp()),
        "nbf": int(now.timestamp()),
        "iat": int(now.timestamp())
    }

    try:
        return jwt.encode(
            token, cert_private_key, algorithm="RS256", headers={"x5t": thumbprint}
        )
    except Exception as e:
        raise ValueError(f"Error creating JWT assertion: {e}")

def get_access_token(tenant_id, client_id, cert_path, cert_password, thumbprint):
    """
    Get an OAuth 2.0 access token using a certificate.
    """
    try:
        private_key = load_private_key(cert_path, cert_password.encode() if cert_password else None)
        jwt_assertion = create_jwt_assertion(tenant_id, client_id, private_key, thumbprint)
    except Exception as e:
        raise ValueError(f"Error in authentication setup: {e}")

    payload = {
        'grant_type': 'client_credentials',
        'client_assertion': jwt_assertion,
        'client_assertion_type': 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
        'scope': f"https://{tenant_id}.sharepoint.com/.default"
    }

    response = requests.post(f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token", data=payload)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise ValueError(f"Error getting access token: {response.status_code} {response.text}")

def make_api_request(access_token, url):
    """
    Make an authenticated GET request to the SharePoint API.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json;odata=verbose"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Error with API request: {response.status_code} {response.text}")