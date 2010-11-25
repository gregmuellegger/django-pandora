django-pandora
==============

*This is Pandora's box. Don't open it if you cannot live with the
consequences.*

**django-pandora** is a utility library for django that lets you easily store
values in a thread-local. This makes it possible to introduce global variables
that are thread safe and don't interfere with other requests to the server.

However a global state is a common anti-pattern in software development that
you usually want to avoid. But at the end of the day it might be the easiest
way to solve some of your problems.

The most common use case for **django-pandora** might be to store the current
request in Pandora's box to make it available in places of your code that
doesn't get the request passed in as argument.

Installation
------------

#. ``pip install django-pandora``
#. Add ``'pandora.middleware.RequestMiddleware'`` to your
   ``MIDDLEWARE_CLASSES`` setting. (optional)

Usage
-----

The ``pandora.box`` object implements a dict like interface which you can use
to store thread local values. It's really as simple as using a dictionary::

    >>> from pandora import box
    >>> box['foo'] = 'Hello world!'
    >>> box['foo']
    'Hello world!'
    >>> 'foo' in box
    True
    >>> 'bar' in box
    False
    >>> box['bar']
    Traceback (most recent call last):
      ...
    KeyError: 'bar'
    >>> box.get('bar', None)
    None

As mentioned above, you might want to use the box to store the current request
object. Pandora ships with a custom middleware for this purpose. Just append
``'pandora.middleware.RequestMiddleware'`` to your ``MIDDLEWARE_CLASSES``
setting. You can then access the request with ``box['request']``.

There is also another middleware that stores the current user object in
``box['user']``. To use this, add ``'pandora.middleware.UserMiddleware'`` to
your ``MIDDLEWARE_CLASSES`` setting, but make sure that it is listed *after*
``'django.contrib.auth.middleware.AuthenticationMiddleware'``.

Tips
----

* You don't need to import the box object into your module if you think the name
  is too generic and might clash with some of your local names. Just use ::

    >>> import pandora
    >>> pandora.box['request']
    ...

* Even if opening Pandora's box might not seem too evil at the first glance,
  please try to avoid it and pass the request object or any other dependency
  around where possible. Having a global state makes things more difficult for
  everyone - especially to reliably test your code.

* Read the `Wikipedia article about Pandora's box
  <http://en.wikipedia.org/wiki/Pandora's_box>`_.
