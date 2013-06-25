#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2013, Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


try:
    from http.client import HTTPException
except ImportError:
    from httplib import HTTPException


class NetworkAddressError(IOError):

    def __init__(self, socket_error, netloc=None):
        self.netloc = netloc
        if self.netloc:
            message = "{0} [{1}]".format(socket_error.args[1], self.netloc)
        else:
            message = socket_error.args[1]
        IOError.__init__(self, message)
        self.__cause__ = socket_error


class TooManyRedirects(HTTPException):
    pass
