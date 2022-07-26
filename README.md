[![build-and-tests](https://github.com/Szczaleg/django-symmetric-fields/actions/workflows/django.yml/badge.svg)](https://github.com/Szczaleg/django-symmetric-fields/actions/workflows/django.yml)

# Django Symmetric Fields

This package provides encrypted model fields in Django using symmetric fernet encryption.

# Getting started
### Package installation
```shell
$ pip install django-symmetric-fields
```
### Keys
```django-symmetric-fields``` uses fernet keys from ```settings.py``` for encryption. Provide a list of keys in the ```DSF_ENCRYPTION_KEYS``` setting. E.g:

```python
DSF_ENCRYPTION_KEYS = [
    b"key1",
    b"key2",
]
```

Package supports key rotation. A newest key in the front of the list is used to encrypt new data, while the later ones assure that the old encrypted data can still be read.

# Usage

After you've completed the initial installation and provided keys in ```settings.py``` you can import your new fernet fields like any other:

```python
from symmetricfields.fields import FernetEncryptedTextField

class ModelWithEncryptedField(models.Model):
    encrypted_field = FernetEncryptedTextField()
```

### Retrieving values
Each field is provided with two properties used to retrieve the values of the fields ```value``` and ```decrypted```. The values are not decrypted until explicitly requested.

```python
ModelWithEncryptedField.objects.create(encrypted_field='test')

my_new_encrypted_object = ModuleWithEncryptedField.objects.first()
my_new_encrypted_object.encrypted_field.value  # returns encrypted value of the field
my_new_encrypted_object.encrypted_field.decrypted  # returns 'test'
```



### Supports
python >= 3.7, django>=3.1

requires cryptography >= 0.9