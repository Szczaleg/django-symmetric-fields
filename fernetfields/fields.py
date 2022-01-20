from contextlib import suppress

from .crypters import FernetCrypter
from django.conf import settings
from django.db import models
from cryptography.fernet import InvalidToken


class FernetEncyptedMixin:
    # STRING_ENCODING = getattr(settings, 'STRING ENCODING', 'utf-8')
    STRING_ENCODING = 'utf-8'

    def __init__(self, show_values=False, *args, **kwargs):
        self.show_values = show_values
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            return value
        if self.show_values:
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

    # def formfield(self, **kwargs):
    #     kwargs['widget'] = ReadOnlyPasswordHashWidget
    #     print(kwargs)
    #     return super(FernetEncyptedMixin, self).formfield(**kwargs)


class FernetEncryptedTextField(FernetEncyptedMixin, models.TextField):
    pass


class FernetEncryptedBigIntegerField(FernetEncyptedMixin, models.BigIntegerField):
    pass


class FernetEncryptedSmallIntegerField(FernetEncyptedMixin, models.SmallIntegerField):
    pass


class FernetEncryptedIPAddressField(FernetEncyptedMixin, models.IPAddressField):
    pass


class FernetEncryptedNullBooleanField(FernetEncyptedMixin, models.NullBooleanField):
    pass


class FernetEncryptedTimeField(FernetEncyptedMixin, models.TimeField):
    pass


class FernetEncryptedBinaryField(FernetEncyptedMixin, models.BinaryField):
    pass


class FernetEncryptedUUIDField(FernetEncyptedMixin, models.UUIDField):
    pass


class FernetEncryptedCharField(FernetEncyptedMixin, models.CharField):
    pass


class FernetEncryptedDateField(FernetEncyptedMixin, models.DateField):
    pass


class FernetEncryptedDateTimeField(FernetEncyptedMixin, models.DateTimeField):
    pass


class FernetEncryptedEmailField(FernetEncyptedMixin, models.EmailField):
    pass


class FernetEncryptedBooleanField(FernetEncyptedMixin, models.BooleanField):
    pass
