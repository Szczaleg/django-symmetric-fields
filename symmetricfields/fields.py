from django.db import models
from . import mixins, values


class FernetEncryptedTextField(mixins.FernetEncryptedMixin, models.TextField):
    pass


class FernetEncryptedBigIntegerField(
    mixins.FernetEncryptedIntegerMixin, models.BigIntegerField
):
    pass


class FernetEncryptedIntegerField(
    mixins.FernetEncryptedIntegerMixin, models.IntegerField
):
    pass


class FernetEncryptedSmallIntegerField(
    mixins.FernetEncryptedIntegerMixin, models.SmallIntegerField
):
    pass


class FernetEncryptedIPAddressField(mixins.FernetEncryptedMixin, models.IPAddressField):
    pass


class FernetEncryptedNullBooleanField(
    mixins.FernetEncryptedBoolMixin, models.NullBooleanField
):
    pass


class FernetEncryptedBinaryField(mixins.FernetEncryptedMixin, models.BinaryField):
    pass


class FernetEncryptedUUIDField(mixins.FernetEncryptedMixin, models.UUIDField):
    def to_python(self, value):
        if not value:
            return value
        return values.UUIDFieldValue(value)


class FernetEncryptedCharField(mixins.FernetEncryptedMixin, models.CharField):
    def to_python(self, value):
        if not value:
            return value
        return values.TimeFieldValue(value)


class FernetEncryptedTimeField(mixins.FernetEncryptedTimeMixin, models.TimeField):
    def to_python(self, value):
        if not value:
            return value
        return values.TimeFieldValue(value)


class FernetEncryptedDateField(mixins.FernetEncryptedMixin, models.DateField):
    def to_python(self, value):
        if not value:
            return value
        return values.DateFieldValue(value)


class FernetEncryptedDateTimeField(
    mixins.FernetEncryptedTimeMixin, models.DateTimeField
):
    def to_python(self, value):
        if not value:
            return value
        return values.DateTimeFieldValue(value)


class FernetEncryptedEmailField(mixins.FernetEncryptedMixin, models.EmailField):
    pass


class FernetEncryptedBooleanField(mixins.FernetEncryptedBoolMixin, models.BooleanField):
    pass
