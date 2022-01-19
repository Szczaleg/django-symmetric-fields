from contextlib import suppress
from django.contrib.admin.widgets import AdminFileWidget
from .crypters import FernetCrypter
from django.conf import settings
from django.db import models
from cryptography.fernet import InvalidToken
fernet_crypter = FernetCrypter()
from django.contrib.auth.models import User

class FernetEncyptedMixin:
    STRING_ENCODING = getattr(settings, 'STRING ENCODING', 'utf-8')

    def __init__(self, show_values=False, *args, **kwargs):
        self.show_values = show_values
        if not self.show_values:
            kwargs['editable'] = False
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            return value
        if self.show_values:
            with suppress(InvalidToken):
                value = fernet_crypter.decrypt(value)
        return super(FernetEncyptedMixin, self).to_python(value)

    def get_db_prep_save(self, value, connection):
        value = super(FernetEncyptedMixin, self).get_db_prep_save(value, connection)
        if not value:
            return value
        return fernet_crypter.encrypt(value)

    def from_db_value(self, value, *args, **kwargs):
        return self.to_python(value)

    def formfield(self, **kwargs):
        print("XDDDDDDDDDDDDDDDDDDd")
        print(kwargs)
        return super().formfield()


class FernetEncryptedTextField(FernetEncyptedMixin, models.TextField):
    pass