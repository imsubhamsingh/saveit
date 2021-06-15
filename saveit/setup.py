from setuptools import setup

setup(
    name="saveit",
    verson="1.0",
    author="Subham Singh",
    author_email="imsks007@gmail.com",
    description="A cli utility to write text ina a file",
    py_modules=["saveit"],
    url="https://github.com/imsubhamsingh/saveit",
    issues="https://github.com/imsubhamsingh/saveit/issues",
    license="MIT License",
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        saveit=saveit:cli
    """,
)
