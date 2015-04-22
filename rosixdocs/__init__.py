# -*- coding: utf-8 -*-
#
#   Copyright 2015 Grigoriy Kramarenko <root@rosix.ru>
#
#   This file is part of RosixDocs.
#
#   RosixDocs is free software: you can redistribute it and/or
#   modify it under the terms of the GNU Affero General Public License
#   as published by the Free Software Foundation, either version 3 of
#   the License, or (at your option) any later version.
#
#   RosixDocs is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public
#   License along with RosixDocs. If not, see
#   <http://www.gnu.org/licenses/>.
#
import os

VERSION = (0, 0, 1)

def get_version(*args, **kwargs):
    return '%d.%d.%d' % VERSION

def get_docs_version(*args, **kwargs):
    return '%d.%d' % VERSION[:2]

__version__ = get_version()


def get_themes_path():
    """ Returns path to included themes. """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), 'themes'))

