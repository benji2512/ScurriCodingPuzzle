from setuptools import find_packages, setup

setup(
    name='postcode_validator',
    packages=find_packages(include=['postcode_validator']),
    version='0.1.0',
    description='A postcode validator',
    author='Me',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
