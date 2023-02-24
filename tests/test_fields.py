import datetime
import uuid

from tests import models
import pytest


@pytest.mark.parametrize(
    "test_model, test_value",
    [
        (models.TestIntegerFieldModel, 2147483647),
        (models.TestSmallIntegerFieldModel, -32768),
        (models.TestBigIntegerFieldModel, 9223372036854775807),
        (models.TestDateTimeFieldModel, datetime.datetime(2069, 4, 20, 21, 37)),
        (models.TestDateFieldModel, datetime.date.fromisoformat("2069-04-20")),
        (models.TestTimeFieldModel, datetime.time.fromisoformat("04:20")),
        (models.TestUUIDFieldModel, uuid.uuid4()),
        (models.TestIPAddressFieldModel, "127.0.0.1"),
        (models.TestEmailFieldModel, "test@test.test"),
        (models.TestTextFieldModel, "test"),
        (models.TestCharFieldModel, "test"),
        (models.TestNullBooleanFieldModel, True),
        (models.TestNullBooleanFieldModel, False),
        (models.TestJsonFieldModel, {"a": [1, 2, 3], "b": True}),
    ],
)
@pytest.mark.django_db
def test_nullable_field(test_model, test_value):
    assert test_model.objects.count() == 0
    test_model.objects.create(test_field=test_value)

    test_object = test_model.objects.first()

    assert test_object.test_field.value != test_value
    assert test_object.test_field.decrypted == test_value

    test_object.test_field = None
    test_object.save()
    test_object.refresh_from_db()
    test_object.save()  # tests save function on unchanged models

    assert test_object.test_field.value is None
    assert test_object.test_field.decrypted is None
