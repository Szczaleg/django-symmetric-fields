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
from fernetfields.fields import FernetEncryptedTextField

class ModelWithEncryptedField(models.Model):
    encrypted_field = FernetEncryptedTextField()
```

### Showing values
By default your data is encrypted and isn't decrypted while accesing it. This can be changed by a passing ```show_values=True``` arguement into the field:

```python
from fernetfields.fields import FernetEncryptedTextField

class ModelWithEncryptedField(models.Model):
    encrypted_field = FernetEncryptedTextField(show_values=True)
```

Fields created this way are encrypted only in the database, if you try read the data in anyway (let it be viewing the model in the django admin or accessing the field value) the value will be decrypted.


### Supports
python >= 3.7, django>=2.0

requires cryptography >= 0.9