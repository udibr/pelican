import sys

if len(sys.argv) != 2:
	print "Usage: %s <file-name>"%sys.argv[0]
	exit(0)
fname = sys.argv[1]

import json

with open(fname,'r') as fp:
    d = json.load(fp)

def filter(d):
    if isinstance(d,dict):
        d = dict((k,[] if k == 'outputs' else filter(v)) for k,v in d.iteritems() if k != 'prompt_number')
    elif isinstance(d,list):
        d = map(filter,d)
    return d

d = filter(d)

with open(fname, 'w') as fp:
    json.dump(d, fp, sort_keys=True, indent=4, separators=(',', ': '))

