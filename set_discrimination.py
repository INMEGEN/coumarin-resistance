import pickle
from sample_data import controls, resistant

p = pickle.load(open('anticoagulantes_final.ann.cons.vcf.gz_varsets.pickle'))

resistant_set = set.intersection(*[set(p[sample]) for sample in resistant])
control_set   = set.union(*[set(p[sample]) for sample in controls])

interesting = resistant_set - control_set

print "r",len(resistant_set)
print "c",len(control_set)

from pprint import pprint
pprint(interesting)
