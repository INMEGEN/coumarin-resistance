import vcf
import argparse
import pickle

parser = argparse.ArgumentParser(description='load variation from a vcf into a dictionary of sets, pickle it')
parser.add_argument("vcf", type=argparse.FileType('r'))
args = parser.parse_args()


vcfr = vcf.Reader(args.vcf)
varsets = {}

for v in vcfr:
    for s in v.samples:
        if s.called:
            if s.sample in varsets:
                varsets[s.sample].add((v.CHROM, v.POS, v.REF, str(v.ALT)))
            else:
                varsets[s.sample]=set([(v.CHROM, v.POS, v.REF, str(v.ALT)),])

pickle.dump( varsets, open( args.vcf.name + "_varsets.pickle", "w" ))
