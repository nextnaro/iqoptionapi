"""The python wrapper for IQ Option API package setup."""
from setuptools import (setup, find_packages)
from pyqoptionapi.version_control import api_version

setup(
    name="pyqoptionapi",
    version=api_version,
    packages=find_packages(),
    install_requires=["pylint", "requests", "websocket-client==0.56"],
    include_package_data=True,
    description="Best & Updated IQ Option API for Python",
    long_description="Best & Updated IQ Option API for Python",
    url="https://github.com/luckyscooby/pyqoptionapi",
    author="Michael Leocádio",
    zip_safe=False
)
