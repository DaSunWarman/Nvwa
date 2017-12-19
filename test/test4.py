class obj(object):
    def out(self):
        print "haha"

# create_obj = compile('obj()', 'create_obj.py', 'eval')
# # a = eval('obj()')
# # a.out()
# a = eval(create_obj)
# a.out()

import importlib
s = 'Sample'
# from packages.Sample.src.Sample import Sample
m = importlib.import_module('packages.'+ s + '.src.'+ s)
# oo = m.Sample()
sobj = eval('m.'+ s +'()')