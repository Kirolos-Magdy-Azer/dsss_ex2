# setup.py
from setuptools import setup, find_packages

setup(
    name="dsss_ex2",
    version="0.1",
    author="Kirolos Magdy Azer",
    author_email="kerolos.m.azer@gmail.com",
    description="a simple calculator for 2 random variables",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Kirolos-Magdy-Azer/dsss_ex2",
    packages=find_packages(),
    install_requires=[
         "requests>=2.20.0" # HTTP library for making API calls
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
