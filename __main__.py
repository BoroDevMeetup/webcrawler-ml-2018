import argparse
import crawler

parser = argparse.ArgumentParser()
parser.add_argument("entry_point", help="Entry point for webcrawler (e.g. https://www.google.com)", type=str)
parser.add_argument("max_pages", help="Maximum pages to crawl", type=int)
args = parser.parse_args()
crawl = crawler.crawl
crawl(args.entry_point,args.max_pages)