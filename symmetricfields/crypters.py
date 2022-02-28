import binascii

from . import exceptions
from django.conf import settings
from cryptography.fernet import Fernet, MultiFernet


class FernetCrypter:
    def __init__(self):
        self.string_encoding = getattr(settings, "STRING ENCODING", "utf-8")
        self.keys = getattr(settings, "DSF_ENCRYPTION_KEYS", None)
        if not self.keys:
            raise exceptions.NoKeysDefinedException()
        if type(self.keys) == list:
            if not self.check_keys(self.keys):
                raise exceptions.InvalidKeyException()
            self.fernet = MultiFernet([Fernet(key) for key in self.keys])
        elif type(self.keys) == bytes:
            if not self.check_key(self.keys):
                raise exceptions.InvalidKeyException()
            self.fernet = Fernet(self.keys)

    def check_keys(self, keys: list) -> bool:
        return all(self.check_key(_key) for _key in keys)

    def check_key(self, key: bytes) -> bool:
        try:
            Fernet(key)
        except binascii.Error:
            return False
        return True

    def encrypt_string(self, _object: str) -> str:
        data = _object.encode(self.string_encoding)
        return self.fernet.encrypt(data).decode(self.string_encoding)

    def encrypt_bytes(self, _object: bytes) -> bytes:
        return self.fernet.encrypt(_object)

    def decrypt_string(self, _object: str) -> str:
        data = _object.encode(self.string_encoding)
        return self.fernet.decrypt(data).decode(self.string_encoding)

    def decrypt_bytes(self, _object: bytes) -> bytes:
        # with suppress(InvalidToken):
        return self.fernet.decrypt(_object)

    def encrypt(self, _object):
        if not _object:
            return _object
        if isinstance(_object, bytes):
            return self.encrypt(_object)
        else:
            return self.encrypt_string(str(_object))

    def decrypt(self, _object):
        if not _object:
            return _object
        if isinstance(_object, bytes):
            return self.decrypt(_object)
        else:
            return self.decrypt_string(str(_object))
