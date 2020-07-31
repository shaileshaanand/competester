from setuptools import setup, find_packages
import pathlib
HERE = pathlib.Path(__file__).parent
README_path = (HERE / "README.md")
with open(README_path, "r", errors="ignore") as README_file:
    README = README_file.read()
setup(
    name='competest',
    version='0.0.11',
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
    description="A python cli tool to test competitive programming solutions(code) against multiple test cases and measure execution time.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/shaileshaanand/competester",
    license="GPL-3.0 License",
    python_requires=">=3.7",
    keywords=["competitive-programming", "testing", "coding"]
)
