import os
import re
import sys
import setuptools
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


PKG_DIR = os.path.dirname(__file__)
with open(os.path.join(PKG_DIR, 'ipfs', '__init__.py')) as VERSION_FILE:
    VERSION = (re.compile(r".*__version__ = '(.*?)'", re.S)
                 .match(VERSION_FILE.read())
                 .group(1))


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as README_FILE:
    README = README_FILE.read()


setuptools.setup(
    name='ipfs',
    description='An implementation of IPFS in Python',
    long_description=README,
    author='bmcorser',
    author_email='bmcorser@gmail.com',
    version=VERSION,
    packages=setuptools.find_packages(),
    tests_require=['pytest'],
    install_requires=['six'],
    cmdclass={'test': PyTest},
)
