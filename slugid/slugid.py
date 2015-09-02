# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import uuid
import base64

def encode(uuid_):
    """
    Returns the given uuid as a 22 character slug. This can be a regular v4
    slug or a "nice" slug.
    """
    bytes = uuid_.bytes
    slug = base64.urlsafe_b64encode(str(bytes))[:22] # Drop '==' padding
    return slug


def decode(slug):
    """
    Returns the uuid represented by the given v4 or "nice" slug
    """
    bytes = base64.urlsafe_b64decode(slug + "==")  # Add '==' padding
    return uuid.UUID(bytes=bytes)


def v4():
    """
    Returns a randomly generated uuid v4 compliant slug
    """
    bytes = uuid.uuid4().bytes
    slug = base64.urlsafe_b64encode(str(bytes))[:22] # Drop '==' padding
    return slug


def nice():
    """
    Returns a randomly generated uuid v4 compliant slug which conforms to a set
    of "nice" properties, at the cost of some entropy. Currently this means one
    extra fixed bit (the first bit of the uuid is set to 0) which guarantees the
    slug will begin with [A-Za-f]. For example such slugs don't require special
    handling when used as command line parameters (whereas non-nice slugs may
    start with `-` which can confuse command line tools).

    Potentially other "nice" properties may be added in future to further
    restrict the range of potential uuids that may be generated.
    """
    bytes = uuid.uuid4().bytes
    bytes = chr(ord(bytes[0]) & 0x7f) + bytes[1:]  # Ensure slug starts with [A-Za-f]
    slug = base64.urlsafe_b64encode(str(bytes))[:22]  # Drop '==' padding
    return slug
