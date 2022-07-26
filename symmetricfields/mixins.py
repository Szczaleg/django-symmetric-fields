import json

from . import values
from .crypters import FernetCrypter
from cryptography.fernet import InvalidToken


class FernetEncryptedMixin:
    def to_python(self, value):
        if not value:
            return values.FieldValue(value)
        super_value = super(FernetEncryptedMixin, self).to_python(value)
        return values.FieldValue(super_value)

    def get_db_prep_save(self, value, connection):
        prep_value = super(FernetEncryptedMixin, self).get_db_prep_save(
            value, connection
        )
        if isinstance(value, values.FieldValue):
            value = prep_value.value
        fernet_crypter = FernetCrypter()
        try:
            fernet_crypter.decrypt(value)
        except InvalidToken:
            return fernet_crypter.encrypt(value)
        return value

    def from_db_value(self, value, *args, **kwargs):
        return self.to_python(value)

    def get_internal_type(self):
        return "TextField"


class FernetEncryptedBoolMixin(FernetEncryptedMixin):
    def get_db_prep_save(self, value, connection):
        if value is None:
            return None
        fernet_crypter = FernetCrypter()
        try:
            fernet_crypter.decrypt_string(str(value))
        except InvalidToken:
            if value is True:
                value = "1"
            elif value is False:
                value = "0"
            return fernet_crypter.encrypt_string(str(value))
        return value

    def to_python(self, value):
        return values.BooleanFieldValue(value)


class FernetEncryptedIntegerMixin(FernetEncryptedMixin):
    def to_python(self, value):
        return values.IntegerFieldValue(value)


class FernetEncryptedTimeMixin(FernetEncryptedMixin):
    def get_db_prep_save(self, value, connection):
        if not value:
            return value
        fernet_crypter = FernetCrypter()
        try:
            fernet_crypter.decrypt(value)
        except InvalidToken:
            value = fernet_crypter.encrypt(value)
        return value


class FernetEncryptedJSONMixin(FernetEncryptedMixin):
    def get_db_prep_save(self, value, connection):
        if value is None:
            return None
        fernet_crypter = FernetCrypter()
        try:
            fernet_crypter.decrypt_string(str(value))
        except InvalidToken:
            return fernet_crypter.encrypt_string(json.dumps(value))
        return value

    def to_python(self, value):
        return values.JSONFieldValue(value)
