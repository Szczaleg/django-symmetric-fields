from tests.models import TestTextFieldModel
import pytest


@pytest.mark.django_db
def test_text_field():
    test_object = TestTextFieldModel.objects.create(test_field='test_field', hidden_test_field='hidden_test_field')
    assert test_object.test_field == 'test_field'
    assert test_object.hidden_test_field != 'test_field'
