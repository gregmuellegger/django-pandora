'''
This is Pandora's box. Don't open it if you cannot live with the
consequences.

More about Pandora's box: http://en.wikipedia.org/wiki/Pandora's_box


Usage:

>>> from pandora import box
>>> box['user'] = user

In a totally different stack frame while peforming the same request:

>>> from pandora import box
>>> user = box['user']

Be aware that the access to a variable might raise a ``KeyError`` if it was
not set yet for the current thread. You can use the dict's get method to
return a sensible default if the key is not available:

>>> user = box.get('user', AnonymousUser())
'''

from UserDict import UserDict
try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local


class Box(UserDict):
    '''
    Be aware ... you are about to let all the evil into your application!

    ``Box`` is a dict-like object that stores its content in a thread local.

    You can use this to store global variables like django's request in a
    context that is only accessible by the current thread.
    '''
    def __init__(self):
        self._local = local()
        self.data = self._local.__dict__


box = Box()
