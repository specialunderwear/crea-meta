import argparse

from creameta.meta import JSONMetaNonsence
from os.path import join, dirname


def reveal_source(relative_path):
    habitat = dirname(__file__)
    print "contents of %s" % relative_path
    return "".join(map(lambda x: ">>> %s" % x, open(join(habitat, relative_path))))

def main():
    p = argparse.ArgumentParser(description='Being creative with __metaclass__')
    p.add_argument('demo', choices=['json', 'watching'])
    
    args = p.parse_args()
    if args.demo == 'json':
        print reveal_source('demo/json.py')
        import creameta.demo.json
    elif args.demo == 'watching':
        import creameta.demo.watching
