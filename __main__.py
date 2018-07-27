import argparse
import crawler

parser = argparse.ArgumentParser()
parser.add_argument("entry_point", help="Entry point for webcrawler (e.g. https://www.google.com)", type=str)
parser.add_argument("--max_pages", help="Maximum pages to crawl, default 10", type=int)
parser.add_argument("--restrict_domain", help="Restrict navigation to root domain (True or False), default: True", type=bool)
args = parser.parse_args()
print("Beginning to crawl...")
if args.max_pages: print("Max pages to crawl set to {}".format(args.max_pages))
print("Restricting domain") if args.restrict_domain else print("Domain not restricted\n...\n")
crawl = crawler.crawl
crawl(args.entry_point,args.max_pages,args.restrict_domain)