from contextlib import suppress
from uuid import UUID
from datetime import time, date, datetime
from .crypters import FernetCrypter
from cryptography.fernet import InvalidToken


class FieldValue:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def _decrypt_value(self):
        if not self.value:
            return self.value
        crypter = FernetCrypter()
        with suppress(InvalidToken):
            value = crypter.decrypt(self.value)
        return value

    @property
    def decrypted(self):
        return self._decrypt_value()


class BooleanFieldValue(FieldValue):
    @property
    def decrypted(self):
        value = self._decrypt_value()
        if value == "None":
            return None
        return value == "1"


class IntegerFieldValue(FieldValue):
    @property
    def decrypted(self):
        return int(self._decrypt_value())


class UUIDFieldValue(FieldValue):
    @property
    def decrypted(self):
        return UUID(self._decrypt_value())


class TimeFieldValue(FieldValue):
    @property
    def decrypted(self):
        return time.fromisoformat(self._decrypt_value())


class DateFieldValue(FieldValue):
    @property
    def decrypted(self):
        return date.fromisoformat(self._decrypt_value())


class DateTimeFieldValue(FieldValue):
    @property
    def decrypted(self):
        return datetime.fromisoformat(self._decrypt_value())
