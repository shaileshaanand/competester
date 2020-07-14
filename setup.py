from setuptools import setup, find_packages

setup(
    name='competest',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        competest=competest.competest:competest
    ''',
    author="Shailesh Aanand",
    author_email="anaandshailu@gmail.com",
    description="A python cli tool to test a program against test cases for some desired output."
)
