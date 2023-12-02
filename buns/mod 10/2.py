import re
import requests


def get_headers(url):
    response = requests.get(url)
    html = response.text

    pattern = r'<h3(?:\s+.*?)*?>(.*?)</h3>'
    headers = re.findall(pattern, html)

    return headers


url = 'http://www.columbia.edu/~fdc/sample.html'
headers = get_headers(url)
print(headers)