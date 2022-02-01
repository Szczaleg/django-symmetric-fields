from fernetfields import fields
from django.db.models import Model


class TestTextFieldModel(Model):
    test_field = fields.FernetEncryptedTextField(show_values=True)
    hidden_test_field = fields.FernetEncryptedTextField()


class TestBigIntegerFieldModel(Model):
    test_field = fields.FernetEncryptedBigIntegerField(show_values=True)
    hidden_test_field = fields.FernetEncryptedBigIntegerField()


class TestSmallIntegerFieldModel(Model):
    test_field = fields.FernetEncryptedSmallIntegerField(show_values=True)
    hidden_test_field = fields.FernetEncryptedSmallIntegerField()


class TestIntegerFieldModel(Model):
    test_field = fields.FernetEncryptedIntegerField(show_values=True)
    hidden_test_field = fields.FernetEncryptedIntegerField()


class TestIPAddressFieldModel(Model):
    test_field = fields.FernetEncryptedIPAddressField(show_values=True)
    hidden_test_field = fields.FernetEncryptedIPAddressField()


class TestNullBooleanFieldModel(Model):
    test_field = fields.FernetEncryptedNullBooleanField(show_values=True)
    hidden_test_field = fields.FernetEncryptedNullBooleanField()


class TestTimeFieldModel(Model):
    test_field = fields.FernetEncryptedTimeField(show_values=True)
    hidden_test_field = fields.FernetEncryptedTimeField()


class TestBinaryFieldModel(Model):  #untested
    test_field = fields.FernetEncryptedBinaryField(show_values=True)
    hidden_test_field = fields.FernetEncryptedBinaryField()


class TestUUIDFieldModel(Model):
    test_field = fields.FernetEncryptedUUIDField(show_values=True)
    hidden_test_field = fields.FernetEncryptedUUIDField()


class TestDateFieldModel(Model):
    test_field = fields.FernetEncryptedDateField(show_values=True)
    hidden_test_field = fields.FernetEncryptedDateField()


class TestDateTimeFieldModel(Model):
    test_field = fields.FernetEncryptedDateTimeField(show_values=True)
    hidden_test_field = fields.FernetEncryptedDateTimeField()


class TestEmailFieldModel(Model):
    test_field = fields.FernetEncryptedEmailField(show_values=True)
    hidden_test_field = fields.FernetEncryptedEmailField()


class TestBooleanFieldModel(Model):
    test_field = fields.FernetEncryptedBooleanField(show_values=True)
    hidden_test_field = fields.FernetEncryptedBooleanField()
