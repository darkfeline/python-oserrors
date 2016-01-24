# Copyright (C) 2015-2016  Allen Li
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

r"""This module contains helpers for properly constructing OSError subclasses.

This module provides one general purpose function, oserror(), for creating
OSError constructor functions.

This module also exports the following pre-made constructor functions, which
return an OSError object with the given error code:

- blocking_io_eagain(): errno.EAGAIN
- blocking_io_ealready(): errno.EALREADY
- blocking_io_ewouldblock(): errno.EWOULDBLOCK
- blocking_io_einprogress(): errno.EINPROGRESS
- child_process(): errno.ECHILD
- broken_pipe_eshutdown(): errno.ESHUTDOWN
- broken_pipe_epipe(): errno.EPIPE
- connection_aborted(): errno.ECONNABORTED
- connection_refused(): errno.ECONNREFUSED
- connection_reset(): errno.ECONNRESET
- file_exists(): errno.EEXIST
- file_not_found(): errno.ENOENT
- interrupted(): errno.EINTR
- is_a_directory(): errno.EISDIR
- not_a_directory(): errno.ENOTDIR
- permission_eacces(): errno.EACCES
- permission_eperm(): errno.EPERM
- process_lookup(): errno.ESRCH
- timeout(): errno.ETIMEDOUT

"""

import errno
import os

_ERRORS = (
    ('blocking_io_eagain', errno.EAGAIN),
    ('blocking_io_ealready', errno.EALREADY),
    ('blocking_io_ewouldblock', errno.EWOULDBLOCK),
    ('blocking_io_einprogress', errno.EINPROGRESS),
    ('child_process', errno.ECHILD),
    ('broken_pipe_eshutdown', errno.ESHUTDOWN),
    ('broken_pipe_epipe', errno.EPIPE),
    ('connection_aborted', errno.ECONNABORTED),
    ('connection_refused', errno.ECONNREFUSED),
    ('connection_reset', errno.ECONNRESET),
    ('file_exists', errno.EEXIST),
    ('file_not_found', errno.ENOENT),
    ('interrupted', errno.EINTR),
    ('is_a_directory', errno.EISDIR),
    ('not_a_directory', errno.ENOTDIR),
    ('permission_eacces', errno.EACCES),
    ('permission_eperm', errno.EPERM),
    ('process_lookup', errno.ESRCH),
    ('timeout', errno.ETIMEDOUT),
)


def oserror(err):
    """Return an OSError builder function.

    err is an error number, as supplied by the errno module.
    Example: errno.ENOENT

    The returned OSError builder function takes three arguments: filename,
    filename2, and written. The meaning and applicability of these arguments
    depend on the error number.

    """
    def build_oserror(filename=None, filename2=None, written=None):
        error = OSError(err, os.strerror(err))
        if filename:
            error.filename = filename
        if filename2:
            error.filename2 = filename2
        if written:
            error.characters_written = written
        return error
    return build_oserror


def _init():
    """Initialize OSError builders."""
    globals_ = globals()
    for name, err in _ERRORS:
        globals_[name] = oserror(err)

_init()
