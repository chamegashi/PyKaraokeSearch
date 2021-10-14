import argparse
from GetKeyRange import keySearch

parser = argparse.ArgumentParser()
parser.add_argument('keywords', type=str, nargs='*')
args = parser.parse_args()

print(keySearch.searchKey(args.keywords))
