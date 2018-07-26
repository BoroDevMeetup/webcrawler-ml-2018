import requests
from collections import namedtuple
from bs4 import BeautifulSoup

def crawl(root, max_pages):
    Link = namedtuple("Link", "parent url title depth")
    current_page = 1
    pages = [Link(parent="root",url=root,title="Root",depth=0)]
    while current_page <= max_pages and len(pages) > 0:
        link_object = pages.pop(0)
        source_code = requests.get(link_object.url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        print("Links for {} page, '{}':\n".format(link_object.title,link_object.url))
        for link in soup.findAll("a"):
            temp_link = Link(parent=link_object.url,url=link.get("href"),title=link.string,depth=link_object.depth + 1)
            print_stats(temp_link)
            pages.append(temp_link)
        print("\n")
        current_page += 1
    print("Current page is {} and max pages is {}".format(current_page - 1,max_pages))
    if current_page -1 < max_pages: print("The number of pages requested is greater than the number of pages avaiable")
    print("Completed")

def print_stats(link_object):
    print("    Parent: {}".format(link_object.parent))
    print("    Title: {}".format(link_object.title))
    print("    Link: {}".format(link_object.url))
    print("    Depth: {}\n".format(link_object.depth))

if __name__ == "__main__":
    crawl('https://www.google.com',3)