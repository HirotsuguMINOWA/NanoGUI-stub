# setup.py
from setuptools import setup

setup(
    name="nanogui-stubs",
    version="0.0.1",
    packages=["nanogui-stubs"],
    package_data={
        "nanogui-stubs": ["*.pyi"],
    },
    install_requires=[
        "nanogui==0.1.4",
    ],
)