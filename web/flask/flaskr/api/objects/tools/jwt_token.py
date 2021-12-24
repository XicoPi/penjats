import datetime
import jwt

class Token(object):
    """
    Session token class definition and implementanion

    Actual token lifetime is about 5 days -> 432000 seconds
    "exp": Expiration time
    "nbf": not (process) before time
    "iss": Issuer
    "aud": audiencie
    "iat": Iussed At (creation time)


    SIGNATURE ALGORITHM: Ed25519
    HASH ALGORITHM: SHA512
    generate: https://www.gniibe.org/memo/software/gpg/keygen-25519.html
    """
    TOKEN_LIFETIME = 432000
    TOKEN_NBF = 0.015
    def __init__(self, payload={}, token="", private_key=b"", public_key=b""):
        self._payload = payload
        self._token = token
        self._private_key = private_key
        self._public_key = public_key

    def _get_token_private_key(self, private_key_filename: str) -> bytes:
        key = ""
        with open(private_key_filename, "r") as private_key_file:
            key = private_key_file.read()
        self._private_key = key.encode("utf-8")
        return self._private_key

    def _get_token_public_key(self, public_key_filename) -> bytes:
        key = ""
        with open(public_key_filename, "r") as public_key_file:
            key = public_key_file.read()
        self._public_key = key.encode("utf-8")
        return self._public_key

    def _generate_token_claims(self, issuer: str, audience: list):
        """
        CLAIMS:
        "exp": Expiration time
        "nbf": not (process) before time -> It's a constant now, in a future more things to implement
        "iss": Issuer
        "aud": audiencie
        "iat": Iussed At -> creation time
        """
        self._payload = {
            "exp": (int(datetime.datetime.now().timestamp()) + self.TOKEN_LIFETIME),
            "nbf": self.TOKEN_NBF, #WIP DoS Atacks??
            "iss": issuer, #ej: session, state...
            "aud": audience, #ej: login_api_processor - communication between services
            "iat": int(datetime.datetime.now().timestamp())
        }

    def get_payload(self) -> dict:
        return self._payload

    def get_token(self) -> str:
        return self._token

    def encode_auth_token(self, issuer: str, audience: list) -> str:
        self._generate_token_claims(issuer, audience)
        self._token = jwt.encode(
            self._payload,
            self._private_key,
            algorithm="RS512"
        )
        return self._token

    def decode_auth_token(self, issuer: str, audience: str) -> dict:
        self._payload = jwt.decode(
            self._token,
            self._public_key,
            algorithms=["RS512"],
            audience=audience,
            issuer=issuer
        )
        return self._payload

    #def check_token_expiration(self) -> bool:
    #    now_time = int(datetime.datetime.now().timestamp())
    #    response = True
    #    if ("creation" in self._payload.keys()):
    #        response = (self._payload["creation"] + self.TOKEN_LIFETIME) < now_time
    #    elif (token != ""):
    #        payload = self.decode_auth_token()
    #        response = (payload["creation"] + self.TOKEN_LIFETIME) < now_time
    #    return response
