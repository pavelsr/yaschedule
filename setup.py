from setuptools import setup, find_packages

with open('requirements.txt', 'r') as file:
    install_requires = [x for x in file.read().splitlines()]

with open('README.md', 'r') as file:
    description = file.read()

version = '0.0.1'

setup(
    name='yaschedule',
    version=version,
    description=description,
    url='https://github.com/StannisGr/yaschedule',
    author='StannisGr',
    license='Apache License 2.0',
    platforms=['any'],
    keywords='yandex, schedule, api',
    packages=find_packages(where='yaschedule'),
    install_requires=install_requires,
)
