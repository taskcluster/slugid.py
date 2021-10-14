# Licensed under the Mozilla Public Licence 2.0.
# https://www.mozilla.org/en-US/MPL/2.0

import sys, uuid, base64

def _ascii(s):
    if sys.version_info.major != 2 and isinstance(s, bytes):
        return s.decode('ascii')
    return s

def encode(uuid_):
    return _ascii(base64.urlsafe_b64encode(uuid_.bytes)[:-2])

def decode(slug):
    return uuid.UUID(bytes=base64.urlsafe_b64decode(_ascii(slug) + '=='))

def v4():
    return encode(uuid.uuid4())

def nice():
    s = v4()
    if s[0] == '-' or s[0] == '_':
      s[0] = 'f'
    return s
