from pathlib import Path

from setuptools import setup, find_packages


with open('requirements.txt',"r") as f:
    requirements = f.read().splitlines()

with open("README.md","r") as f:
    readme = f.read()

ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / 'regression_model'
about = {}
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version


setup(
    name = "regression_AniruddhaMandal",
    version = about['__version__'],
    author = "Aniruddha Mandal",
    author_email = "ani96dh@gmail.com",
    description = "Testing pourpose",
    long_description = readme,
    long_description_content_type = 'text/markdown',
    install_requires = requirements,
    packages = find_packages(exclude=('tests',)),
    python_requires = ">=3.6",
    package_data = {'regression_model' : ['VERSION']},
    include_package_data = True,
)