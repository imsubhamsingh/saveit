from setuptools import setup

setup(
    name="saveit",
    verson="1.0",
    py_modules=['saveit'],
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        saveit=saveit:cli
    """,



)