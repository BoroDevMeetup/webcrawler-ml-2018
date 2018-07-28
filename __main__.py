import argparse
import crawler

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser()
parser.add_argument("entry_point", help="Entry point for webcrawler (e.g. https://www.google.com)", type=str)
parser.add_argument("--max_pages", help="Maximum pages to crawl, default 10", type=int, default=10)
parser.add_argument("--restrict_domain", help="Restrict navigation to root domain (True or False), default: True", type=str2bool, default=True)
args = parser.parse_args()
print("Beginning to crawl...")
if args.max_pages: print("Max pages to crawl set to {}".format(args.max_pages))
print("Domain not restricted") if not args.restrict_domain and args.restrict_domain != None else print("Restricting domain")
print("...\n")
crawl = crawler.crawl
crawl(args.entry_point,args.max_pages,args.restrict_domain)
