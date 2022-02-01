import datetime
from contextlib import suppress
from uuid import UUID

from django.utils.functional import cached_property

from .crypters import FernetCrypter
from django.conf import settings
from django.db import models
from cryptography.fernet import InvalidToken


class FernetEncyptedMixin:

    def __init__(self, show_values=False, *args, **kwargs):
        self.show_values = show_values
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if not value or not self.show_values:
            return value
        fernet_crypter = FernetCrypter()
        with suppress(InvalidToken):
            value = fernet_crypter.decrypt(value)
        return super(FernetEncyptedMixin, self).to_python(value)

    def get_db_prep_save(self, value, connection):
        value = super(FernetEncyptedMixin, self).get_db_prep_save(value, connection)
        if not value:
            return value
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


class FernetEncryptedBoolMixin(FernetEncyptedMixin):

    def get_db_prep_save(self, value, connection):
        fernet_crypter = FernetCrypter()
        try:
            fernet_crypter.decrypt(value)
        except InvalidToken:
            if value is True:
                value = '1'
            elif value is False:
                value = '0'
            return fernet_crypter.encrypt(value)
        return value

    def to_python(self, value):
        if not value or not self.show_values:
            return value
        fernet_crypter = FernetCrypter()
        with suppress(InvalidToken):
            value = fernet_crypter.decrypt(value)
            if value == 'None':
                return
            return value == '1'


class FernetIntegerMixin(FernetEncyptedMixin):

    def to_python(self, value):
        if not value or not self.show_values:
            return value
        fernet_crypter = FernetCrypter()
        with suppress(InvalidToken):
            value = fernet_crypter.decrypt(value)
            return int(value)


class FernetEncryptedTextField(FernetEncyptedMixin, models.TextField):
    pass


class FernetEncryptedBigIntegerField(FernetIntegerMixin, models.BigIntegerField):
    pass


class FernetEncryptedIntegerField(FernetIntegerMixin, models.IntegerField):
    pass


class FernetEncryptedSmallIntegerField(FernetIntegerMixin, models.SmallIntegerField):
    pass


class FernetEncryptedIPAddressField(FernetEncyptedMixin, models.IPAddressField):
    pass


class FernetEncryptedNullBooleanField(FernetEncryptedBoolMixin, models.NullBooleanField):
    pass


class FernetEncryptedTimeField(FernetEncyptedMixin, models.TimeField):

    def get_db_prep_save(self, value, connection):
        if not value:
            return value
        fernet_crypter = FernetCrypter()
        try:
            fernet_crypter.decrypt(value)
        except InvalidToken:
            return fernet_crypter.encrypt(value)
        return value


class FernetEncryptedBinaryField(FernetEncyptedMixin, models.BinaryField):
    pass


class FernetEncryptedUUIDField(FernetEncyptedMixin, models.UUIDField):

    def to_python(self, value):
        if not value or not self.show_values:
            return value
        fernet_crypter = FernetCrypter()
        with suppress(InvalidToken):
            value = fernet_crypter.decrypt(value)
            return UUID(value)


class FernetEncryptedCharField(FernetEncyptedMixin, models.CharField):
    pass


class FernetEncryptedDateField(FernetEncyptedMixin, models.DateField):
    pass


class FernetEncryptedDateTimeField(FernetEncyptedMixin, models.DateTimeField):
    pass


class FernetEncryptedEmailField(FernetEncyptedMixin, models.EmailField):
    pass


class FernetEncryptedBooleanField(FernetEncryptedBoolMixin, models.BooleanField):
    pass
