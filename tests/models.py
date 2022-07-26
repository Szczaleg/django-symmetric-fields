from symmetricfields import fields
from django.db.models import Model


class TestCharFieldModel(Model):
    test_field = fields.FernetEncryptedCharField(null=True)


class TestTextFieldModel(Model):
    test_field = fields.FernetEncryptedTextField(null=True)


class TestBigIntegerFieldModel(Model):
    test_field = fields.FernetEncryptedBigIntegerField(null=True)


class TestSmallIntegerFieldModel(Model):
    test_field = fields.FernetEncryptedSmallIntegerField(null=True)


class TestIntegerFieldModel(Model):
    test_field = fields.FernetEncryptedIntegerField(null=True)


class TestIPAddressFieldModel(Model):
    test_field = fields.FernetEncryptedIPAddressField(null=True)


class TestNullBooleanFieldModel(Model):
    test_field = fields.FernetEncryptedNullBooleanField()


class TestTimeFieldModel(Model):
    test_field = fields.FernetEncryptedTimeField(null=True)


class TestBinaryFieldModel(Model):
    test_field = fields.FernetEncryptedBinaryField(null=True)


class TestUUIDFieldModel(Model):
    test_field = fields.FernetEncryptedUUIDField(null=True)


class TestDateFieldModel(Model):
    test_field = fields.FernetEncryptedDateField(null=True)


class TestDateTimeFieldModel(Model):
    test_field = fields.FernetEncryptedDateTimeField(null=True)


class TestEmailFieldModel(Model):
    test_field = fields.FernetEncryptedEmailField(null=True)


class TestBooleanFieldModel(Model):
    test_field = fields.FernetEncryptedBooleanField()


class TestJsonFieldModel(Model):
    test_field = fields.FernetEncryptedJSONField(null=True)
