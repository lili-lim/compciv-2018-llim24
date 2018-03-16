import requests

def print_hedz(url='https://www.stanford.edu/news/'):
    """
    url can point to any website, but by default, it points to the
    official Stanford News website

    This function does not return anything. It just prints to output.
    """

    txt = fetch_html(url)
    htags = parse_headline_tags(txt)

    for t in htags:
        hedtxt = extract_headline_text(t)
        print(hedtxt)


def extract_headline_text(txt):
    """
    The `txt` argument is a string, ostensibly text that looks like what the HTML
    is for headlines on Stanford's news site, e.g.

        <h3><a href='https://news.stanford.edu/2018/01/1/hello-stanford>Hello Stanford</a></h3>

    This function returns a string, e.g. "Hello Stanford"
    """
    headline = txt.split('>')[2].split('<')[0]
    return headline


def parse_headline_tags(txt):
    """
    The `txt` argument is a string, ostensibly text that looks like the raw HTML
      that can be found at https://wgetsnaps.github.io/stanford-edu-news/news/simple.html

    This function returns a list of strings, each string
        should look like the raw HTML for a standard Stanford news headline, e.g.

          [
            '<h3><a href='https://news.stanford.edu/2018/01/1/hello-stanford>Hello Stanford</a></h3>',
            '<h3><a href='https://news.stanford.edu/2018/01/1/bye-stanford>Bye Stanford</a></h3>'
          ]
    """
    all_lines = txt.splitlines()
    headline_html = list()
    for line in all_lines:
        if "<h3><a" in line:
            headline_html.append(line)
    return headline_html


def fetch_html(url):
    """
    The `url` argument should be string, representing a URL for a webpage

    This function returns another string -- the raw text (i.e. HTML) found at the given URL
    """
    resp = requests.get(url)
    txt = resp.text
    return txt
