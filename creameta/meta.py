import json
import inspect
import hashlib

class JSONMetaNonsenceEncoder(json.JSONEncoder):
    def default(self, obj):
         if obj is JSONMetaNonsence:
             return None
         # Let the base class default method raise the TypeError
         return json.JSONEncoder.default(self, obj)

class JSONMetaNonsence(type):
    def __new__(cls, name, bases, attrs):
        write = attrs.pop('write', None)
        if write is not None:
            with open(name, 'w') as cls_file:
                json.dump(
                    {k:v for k,v in attrs.items() if not k.startswith('__')},
                    cls_file,
                    skipkeys=True,
                    cls=JSONMetaNonsenceEncoder,
                    indent=4
                )
                return hashlib.sha1
        else:
            with open(name) as cls_file:
                loaded_attrs = json.load(cls_file)
                attrs.update(loaded_attrs)
                return type.__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        src = inspect.getsource(cls)
        print "Source of %s\n" % name
        print src
        return type.__init__(cls, name, bases, attrs)


class ImWatchingYou(type):
    def __init__(cls, name, bases, attrs):
        src = inspect.getsource(cls)
        print "checking source of %s\n" % name
        print src
        raw_input("\nPress Enter to continue...\n")
        print "Number of for loops %i" % src.count('for')
        if inspect.getsource(cls).count('for') >= 7:
            import this
            raise Exception("unholy code")
        else:
            print "approved"
        return type.__init__(cls, name, bases, attrs)