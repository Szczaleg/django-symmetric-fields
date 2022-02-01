import datetime
import uuid

from tests import models
import pytest


@pytest.mark.django_db
def test_text_field():
    assert models.TestTextFieldModel.objects.count() == 0
    test_value = 'test'
    models.TestTextFieldModel.objects.create(
        test_field=test_value, hidden_test_field=test_value)

    test_object = models.TestTextFieldModel.objects.first()
    assert test_object.test_field == test_value
    assert test_object.hidden_test_field != test_value


@pytest.mark.django_db
def test_email_field():
    assert models.TestEmailFieldModel.objects.count() == 0
    test_value = 'test@test.test'
    models.TestEmailFieldModel.objects.create(
        test_field=test_value, hidden_test_field=test_value)

    test_object = models.TestEmailFieldModel.objects.first()
    assert test_object.test_field == test_value
    assert test_object.hidden_test_field != test_value


@pytest.mark.django_db
def test_ipadress_field():
    assert models.TestIPAddressFieldModel.objects.count() == 0
    test_value = '127.0.0.1'
    models.TestIPAddressFieldModel.objects.create(
        test_field=test_value, hidden_test_field=test_value)

    test_object = models.TestIPAddressFieldModel.objects.first()
    assert test_object.test_field == test_value
    assert test_object.hidden_test_field != test_value


@pytest.mark.django_db
def test_nullboolean_field():
    assert models.TestNullBooleanFieldModel.objects.count() == 0
    test_value = True
    models.TestNullBooleanFieldModel.objects.create(
        test_field=test_value, hidden_test_field=test_value)

    test_object = models.TestNullBooleanFieldModel.objects.first()
    assert test_object.test_field == test_value
    assert test_object.hidden_test_field != test_value


@pytest.mark.django_db
def test_boolean_field():
    assert models.TestBooleanFieldModel.objects.count() == 0
    test_value = True
    models.TestBooleanFieldModel.objects.create(
        test_field=test_value, hidden_test_field=test_value)

    test_object = models.TestBooleanFieldModel.objects.first()
    assert test_object.test_field == test_value
    assert test_object.hidden_test_field != test_value


@pytest.mark.django_db
def test_nullboolean_field_null_value():
    assert models.TestNullBooleanFieldModel.objects.count() == 0
    test_value = None
    models.TestNullBooleanFieldModel.objects.create(
        test_field=test_value, hidden_test_field=test_value)

    test_object = models.TestNullBooleanFieldModel.objects.first()
    assert test_object.test_field == test_value
    assert test_object.hidden_test_field != test_value


@pytest.mark.django_db
def test_time_field():
    assert models.TestTimeFieldModel.objects.count() == 0
    test_value = datetime.time.fromisoformat('04:20')
    models.TestTimeFieldModel.objects.create(
        test_field=test_value, hidden_test_field=test_value)

    test_object = models.TestTimeFieldModel.objects.first()
    assert test_object.test_field == test_value
    assert test_object.hidden_test_field != test_value


@pytest.mark.django_db
def test_date_field():
    assert models.TestDateFieldModel.objects.count() == 0
    test_value = datetime.date.fromisoformat('2069-04-20')
    models.TestDateFieldModel.objects.create(
        test_field=test_value, hidden_test_field=test_value)

    test_object = models.TestDateFieldModel.objects.first()
    assert test_object.test_field == test_value
    assert test_object.hidden_test_field != test_value


@pytest.mark.django_db
def test_datetime_field():
    assert models.TestDateTimeFieldModel.objects.count() == 0
    test_value = datetime.datetime(2069, 4, 20, 21, 37)
    models.TestDateTimeFieldModel.objects.create(
        test_field=test_value, hidden_test_field=test_value)

    test_object = models.TestDateTimeFieldModel.objects.first()
    assert test_object.test_field == test_value
    assert test_object.hidden_test_field != test_value


@pytest.mark.django_db
def test_bigint_field():
    assert models.TestBigIntegerFieldModel.objects.count() == 0
    test_value = 9223372036854775807
    models.TestBigIntegerFieldModel.objects.create(
        test_field=test_value, hidden_test_field=test_value)

    test_object = models.TestBigIntegerFieldModel.objects.first()
    assert test_object.test_field == test_value
    assert test_object.hidden_test_field != test_value


@pytest.mark.django_db
def test_smallint_field():
    assert models.TestSmallIntegerFieldModel.objects.count() == 0
    test_value = -32768
    models.TestSmallIntegerFieldModel.objects.create(
        test_field=test_value, hidden_test_field=test_value)

    test_object = models.TestSmallIntegerFieldModel.objects.first()
    assert test_object.test_field == test_value
    assert test_object.hidden_test_field != test_value


@pytest.mark.django_db
def test_int_field():
    assert models.TestIntegerFieldModel.objects.count() == 0
    test_value = 2147483647
    models.TestIntegerFieldModel.objects.create(
        test_field=test_value, hidden_test_field=test_value)

    test_object = models.TestIntegerFieldModel.objects.first()
    assert test_object.test_field == test_value
    assert test_object.hidden_test_field != test_value


@pytest.mark.django_db
def test_uuid_field():
    assert models.TestUUIDFieldModel.objects.count() == 0
    test_value = uuid.uuid4()
    models.TestUUIDFieldModel.objects.create(
        test_field=test_value, hidden_test_field=test_value)

    test_object = models.TestUUIDFieldModel.objects.first()
    assert test_object.test_field == test_value
    assert test_object.hidden_test_field != test_value
