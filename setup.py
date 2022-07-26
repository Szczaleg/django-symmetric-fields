from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="django-symmetric-fields",
    version="0.0.7",
    author="Szczaleg",
    description="Symmetric encryption for model fields in Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Szczaleg/django-symmetric-fields",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["symmetricfields"],
    python_requires=">=3.7",
    install_requires=["cryptography"],
)
