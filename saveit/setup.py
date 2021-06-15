import pathlib
from setuptools import setup


HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="saveit",
    verson="1.0.0",
    description="A cli utility to write text ina a file",
    long_description=README,
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
    packages=["saveit"],
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["Click"],
    entry_points={"console_scripts": ["saveit=saveit:cli"]},
)
