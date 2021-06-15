import pathlib
from setuptools import setup


setup(
    name="saveit",
    version="1.2.0",
    description="A utility to write text in a file right from terminal",
    long_description_content_type="text/markdown",
    author="Subham Singh",
    author_email="imsks007@gmail.com",
    url="https://github.com/imsubhamsingh/saveit",
    issues="https://github.com/imsubhamsingh/saveit/issues",
    license="MIT License",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    py_modules=["saveit"],
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["Click"],
    entry_points={"console_scripts": ["saveit=saveit:cli"]},
)
