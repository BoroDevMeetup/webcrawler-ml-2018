import requests
from collections import namedtuple
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import sys

def crawl(root, max_pages, restrict_domain):
    Link = namedtuple("Link", "parent url title depth url_tuple")
    current_page = 1
    root_link = Link(parent="root",url=root,title="Root",depth=0,url_tuple=urlparse(root))
    pages = [root_link]
    while current_page <= max_pages and len(pages) > 0:
        link_object = pages.pop(0)
        if restrict_domain and not same_domain(root_link, link_object): # handle traversal down foreign domains
            print("****** @Edge - will not traverse {} ******\n".format(link_object.url))
            continue
        page_object = parse_page(link_object.url)
        if not page_object: continue
        print("Links for {} page, '{}':\n".format(link_object.title,link_object.url))
        links_found = page_object.findAll("a")
        for link in links_found:
            href = link.get("href")
            temp_link = Link(parent=link_object.url,url=href,title=link.string,depth=link_object.depth + 1,url_tuple=urlparse(href))
            print_stats(temp_link)
            pages.append(temp_link)
        if len(links_found) == 0: print("    No links to display...\n")
        current_page += 1
    print("Current page is {} and max pages is {}".format(current_page - 1,max_pages))
    if current_page - 1 < max_pages: print("The number of pages requested is greater than the number of pages searched")
    print("Completed")

# check if two link objects are within the same domain
def same_domain(root, dest):
    if root.url_tuple.netloc == dest.url_tuple.netloc: return True # true if netlocs are equal
    if not dest.url_tuple.netloc and dest.url_tuple.path: return True # true if the netloc doesn't exist, but path does (self reference)
    if netloc_to_domain(root.url_tuple.netloc) == netloc_to_domain(dest.url_tuple.netloc): return True # true if domain is equal
    return False

# convert netloc to domain
def netloc_to_domain(netloc):
    port_re = re.compile(":\d*")
    netloc_noport = port_re.sub("",netloc) # remove port (if any)
    netloc_split = netloc_noport.split(".")
    if "com" in netloc_split: netloc_split.remove("com")
    l = len(netloc_split)
    if l == 1: return "".join(netloc_split) # if there is only one str in list, it is the domain
    return netloc_split[-1] # else the last item is the domain

# given a url returns a BeautifulSoup page object on success, else returns empty string
def parse_page(url_str):
    try:
        response = requests.get(url_str)
        if response.status_code not in range(200,300):
            print("Response status code for url ({}) not in 200 to 299".format(url_str))
            return ""
        plain_text = response.text
    except:
        print("*********\n  Unexpected error: {}\n  when trying to get {}\n*********".format(sys.exc_info()[0],url_str))
        return ""
    return BeautifulSoup(plain_text, "html.parser")

# prints indented tuple attributes
def print_stats(link_object):
    print("    Parent: {}".format(link_object.parent))
    print("    Title: {}".format(link_object.title))
    print("    Link: {}".format(link_object.url))
    print("    Depth: {}".format(link_object.depth))
    print("    Tuple: {}\n".format(link_object.url_tuple))

if __name__ == "__main__":
    crawl('https://www.google.com',3,True)