import base64
from typing import Final

# https://github.com/Mic92/sops-nix
SECRET_DIR: Final[str] = '/run/secrets'
USER: Final[str] = 'akisamu'


class Secrets:
    uname: Final[str] = open(f'{SECRET_DIR}/chaoxing/{USER}/username').read()
    __password: Final[str] = open(f'{SECRET_DIR}/chaoxing/{USER}/password').read()

    @classmethod
    def get_pass_b64(cls):
        # https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/
        password_bytes: bytes = cls.__password.encode('ascii')
        base64_bytes = base64.b64encode(password_bytes)
        return base64_bytes.decode("ascii")
