#!/usr/bin/env python3
"""Packaging settings."""

from codecs import open
from os.path import abspath, dirname, join

from setuptools import Command, find_packages, setup

from src import __version__

import os

import unittest
import doctest


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    skip_this_docTests = {'filename' : "short description"}

    # options example
    # python setup.py test --module=<modulename>
    # python setup.py test --verbosity=<int>
    user_options = [
        ('module=', None, 'Module name, to run one specific test'),
        ('verbosity=', None, 'verbosity test output')
        ]

    module_list = []

    def initialize_options(self):
        self.module = None
        self.verbosity = 1

    def finalize_options(self):
        if self.module:
            self.module_list.append(self.module)
        else :
            # collect rekursive all python module names from pybill directory (except files that starts with '__')
            for root, dirs, files in os.walk("src", topdown=False):
                for name in files:
                    if name.endswith(".py") and not name.startswith("__"):
                        newname = name.replace('.py','')
                        self.module_list.append(newname)

    def run(self):
        """Run unit integration and doc tests!"""

        if self.module:
            module = self.module
        else:
            module = '*'

        test_loader = unittest.TestLoader()

        suite = test_loader.discover('tests', pattern='%s.py' %module)

        # exclude python modules without doctests
        finder = doctest.DocTestFinder(exclude_empty=False)

        if self.module is None or suite.countTestCases() == 0: # if module was not defined by user 'or' if module was defined by user "and" did not found in tests directory
            for mod_name in self.module_list:
                # check if doctest are skiped
                if mod_name in self.skip_this_docTests.keys():
                    print('s(%s)' %self.skip_this_docTests[mod_name])
                else:
                    # module name is string and it should be executed
                    exec("suite.addTest(doctest.DocTestSuite(%s, test_finder=finder))" %mod_name)

        result = unittest.TextTestRunner(verbosity=int(self.verbosity)).run(suite)

        errNo = 0

        if not result.wasSuccessful():
            errNo = 1

        raise SystemExit(errNo)


class RunStandAloneCodeStyle(Command):
    """Run code style tests."""

    description = 'only checking code style'
    user_options = []

    files_to_be_checked = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        # collect python files
        for root, dirs, files in os.walk("src", topdown=False):
            for name in files:
                if name.endswith(".py") and not name.startswith("__"):
                    newname = name.replace('.py','')
                    self.files_to_be_checked.append("%s/%s" %(root, name))

    def run(self):
        """Run codestyle checks!"""
        # it schould be hier imorted, becouse on setup install -e at empti environment, it trows error
        import pycodestyle

        style = pycodestyle.StyleGuide(ignore=['E501', 'E126', 'E121', 'W503', 'E741' ])
        report = style.check_files(self.files_to_be_checked)

        if report.total_errors:
            raise SystemExit(1)

        raise SystemExit(0)


setup(
    name='<PROJECT NAME>',
    version=__version__,
    description='<DESCRIPTION>',
    long_description=long_description,
    url='https://www.example.com',
    author='Aivars Umbrasko',
    author_email='umbrasko.aivars@gmail.com',
    license='UNLICENSED',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Office',
        'License :: Proprietary',
        'Natural Language :: German',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='rvdinfo, susy, emails',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['docopt', 'sphinx', 'pycodestyle'],
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points={
        'console_scripts': [],
    },
    cmdclass = {'test': RunTests,
                'codestyle': RunStandAloneCodeStyle
                },
)