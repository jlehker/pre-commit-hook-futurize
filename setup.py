from setuptools import setup

setup(
    name='pre_commit_hook_futurize',
    version='0.0.2',
    description='Check if your code is python 3 compatible.',
    install_requires=['future>=0.18.0'],
)

