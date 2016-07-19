from itertools import combinations
import pickle
import argparse
from sample_data import resistant, controls

samples = resistant + controls

plantilla = """
executable     = jinx.py
arguments      = {p1} {p2}
output         = jinx_{s1}_{s2}.out
error          = jinx_{s1}_{s2}.err
log            = jinx_{s1}_{s2}.log                                                    
queue 

"""

with open('pair_jinx_jobs.condor', 'w') as script:
    for pair in combinations(samples, 2):
        script.write(plantilla.format( s1=pair[0],
                                       s2=pair[1],
                                       p1="set_%s.pickle" % pair[0],
                                       p2="set_%s.pickle" % pair[1]))
