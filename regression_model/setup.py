from setuptools import setup, find_packages


with open('requirements.txt',"r") as f:
    requirements = f.read().splitlines()

with open("README.md","r") as f:
    readme = f.read()

with open('regression_model/VERSION', 'r') as f:
    version = f.read()

setup(
    name = "regression_AniruddhaMandal",
    version = version,
    author = "Aniruddha Mandal",
    author_email = "ani96dh@gmail.com",
    description = "Testing pourpose",
    long_description = readme,
    long_description_content_type = 'text/markdown',
    install_requires = requirements,
    packages = find_packages(exclude=('tests',)),
    python_requires = ">=3.6",
)