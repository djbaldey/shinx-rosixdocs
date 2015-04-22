# -*- coding: utf-8 -*-
#
#   Copyright 2012-2015 Grigoriy Kramarenko <root@rosix.ru>
#
#   This file is part of QuickAPI.
#
#   QuickAPI is free software: you can redistribute it and/or
#   modify it under the terms of the GNU Affero General Public License
#   as published by the Free Software Foundation, either version 3 of
#   the License, or (at your option) any later version.
#
#   QuickAPI is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public
#   License along with QuickAPI. If not, see
#   <http://www.gnu.org/licenses/>.
#

from setuptools import setup, find_packages
import rosixdocs

setup(
    name='rosixdocs',
    version=rosixdocs.__version__,
    description='Theme Rosix to the documentation for the Sphinx.',
    long_description=open('README').read(),
    author='Grigoriy Kramarenko',
    author_email='root@rosix.ru',
    url='https://bitbucket.org/djbaldey/rosixdocs',
    license='GNU Affero General Public License v3 or later (AGPLv3+)',
    platforms='any',
    zip_safe=False,
    packages=['rosixdocs'],
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
