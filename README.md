# Overview

This is an open source project created from 'BoroDev Meetup and future meetup(Hack Night).

***

Here are a few TO-DOs before we get started:
[0] Write up goal for projects
[1] Write up Features list
[2] Figure out some form of MVP
[3] Steps to get to milestone
[4] Extra features not included in MVP



https://www.meetup.com/BoroDev/

## Pre-Reqs

1. Clone the repo
2. Install the lastest version python3 ([from Python](https://www.python.org/downloads/release/python-370/) or [brew install](https://docs.python-guide.org/starting/install3/osx/))
3. Follow the steps here to install pipenv [here](https://docs.python-guide.org/dev/virtualenvs/)

## To Test

1. CD into the repo
2. Unzip test-site.zip
3. Setup local webserver using: <pre>`python3 -m http.server`</pre>
4. Run for pre-configured: <pre>`pipenv run python3 crawler.py`</pre> or <pre>`pipenv run python3 . <url-entry-point> --max_pages <number-of-pages> --restrict_domain <bool>`</pre>
   * where *url-entry-point* is a URL (e.g. http://localhost:8000/test-site/a.html), *--max_pages* is an optional int, and *--restrict_domain* is an optional bool
   * example: `pipenv run python3 . http://www.google.com --max_pages 3 --restrict_domain True`