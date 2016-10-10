::

    [master ⚡] $ crea-meta 
    usage: crea-meta [-h] {json,watching}
    crea-meta: error: too few arguments
    (creameta)ebone@mandarijnen-2:~/Projects/crea-meta (.001 MB)  ma okt 10 21:01:08
    [master ⚡] $ crea-meta henk
    usage: crea-meta [-h] {json,watching}
    crea-meta: error: argument demo: invalid choice: 'henk' (choose from 'json', 'watching')
    (creameta)ebone@mandarijnen-2:~/Projects/crea-meta (.001 MB)  ma okt 10 21:01:14
    [master ⚡] $ crea-meta json

contents of demo/json.py::

    >>> from creameta.meta import JSONMetaNonsence
    >>> 
    >>> # create password class that hold passwords
    >>> class passwords(object):
    >>>     __metaclass__ = JSONMetaNonsence
    >>> 
    >>>     henk = 'uy98jjd'
    >>>     piet = 'y98adkkjhd77'
    >>>     kees = 'god'
    >>>     marietje = 'password1'
    >>>     write = True
    >>> 
    >>> # prove that it is stored encrypted
    >>> print passwords
    >>> 
    >>> # create an instance
    >>> a = passwords()
    >>> 
    >>> # prove that all passwords are properly hashed
    >>> print a
    >>> 
    >>> try:
    >>>     # prove that attackers can not read the information out of the passwords
    >>>     # object
    >>>     print a.henk
    >>>     print a.piet
    >>>     print a.kees
    >>>     print a.marietje
    >>> except Exception as e:
    >>>     print e
    >>> 
    >>> raw_input("Press Enter to continue...")
    >>> 
    >>> # create a password class to read the pawwords
    >>> class passwords(object):
    >>>     __metaclass__ = JSONMetaNonsence
    >>> 
    >>>     def __str__(self):
    >>>         return "passwords storage opened"
    >>> 
    >>> # show that this class is of the original type used to store the passwords
    >>> print passwords
    >>> 
    >>> # create an instance to read the passwords
    >>> b = passwords()
    >>> 
    >>> print b
    >>> print dir(b)
    >>> 
    >>> print b.henk
    >>> print b.piet
    >>> print b.kees
    >>> print b.marietje

::

    # prove that it is stored encrypted
    <built-in function openssl_sha1>

    # prove that all passwords are properly hashed
    <sha1 HASH object @ 0x10f8466c0>

    # prove that attackers can not read the information out of the passwords
    '_hashlib.HASH' object has no attribute 'henk'

*Press Enter to continue...*


Source of passwords::

    >>> class passwords(object):
    >>>     __metaclass__ = JSONMetaNonsence
    >>> 
    >>>     henk = 'uy98jjd'
    >>>     piet = 'y98adkkjhd77'
    >>>     kees = 'god'
    >>>     marietje = 'password1'
    >>>     write = True

::

    # show that this class is of the original type used to store the passwords
    <class 'creameta.demo.json.passwords'>
    
    # HUH??
    passwords storage opened
    # WTF!
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__metaclass__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', u'henk', u'kees', u'marietje', u'piet']
    # HELP HELP WIZZARDZ!!
    uy98jjd
    y98adkkjhd77
    god
    password1

::

    (creameta)ebone@mandarijnen-2:~/Projects/crea-meta (.001 MB)  ma okt 10 21:01:28
    [master ⚡] $ crea-meta watching

checking source of PythonClass::

    >>> class PythonClass(object):
    >>>     __metaclass__ = ImWatchingYou
    >>> 
    >>>     def __init__(self, **kwargs):
    >>>         self.__dict__.update(kwargs)
    >>> 
    >>>     def contains(self):
    >>>         for a in self:
    >>>             if a == None:
    >>>                 return "null"


*Press Enter to continue...*

**Number of for loops 1**

::

    approved

*On to the next, press Enter to continue...*

*checking source of AbstractEntityContainerAdapterFactory*

::

    >>> class AbstractEntityContainerAdapterFactory(object):
    >>>     __metaclass__ = ImWatchingYou
    >>> 
    >>>     def __init__(self, **kwargs):
    >>>         self.__dict__.update(kwargs)
    >>> 
    >>>     def contains(self):
    >>>         for a in self:
    >>>             if len(a) != 0:
    >>>                 for b in a:
    >>>                     gosub(b)
    >>>                     for c in b:
    >>>                         for t in c:
    >>>                             for v in t:
    >>>                                 for b in v:
    >>>                                     for n in b:
    >>>                                         for x in n:
    >>>                                             pass


*Press Enter to continue...*

**Number of for loops 8**

::

    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

Haha
----

::

    Traceback (most recent call last):
      File "/Users/ebone/.virtualenvs/creameta/bin/crea-meta", line 8, in <module>
        load_entry_point('crea-meta==0.0.1', 'console_scripts', 'crea-meta')()
      File "/Users/ebone/Projects/crea-meta/creameta/crea.py", line 21, in main
        import creameta.demo.watching
      File "/Users/ebone/Projects/crea-meta/creameta/demo/watching.py", line 19, in <module>
        class AbstractEntityContainerAdapterFactory(object):
      File "/Users/ebone/Projects/crea-meta/creameta/meta.py", line 47, in __init__
        raise Exception("unholy code")
    Exception: unholy code

O lol

::

    (creameta)ebone@mandarijnen-2:~/Projects/crea-meta (.001 MB)  ma okt 10 21:01:45
    [master ⚡] $