import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad requests
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return []
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for link in soup.find_all('a', href=True):
        absolute_url = urljoin(url, link['href'])
        links.append(absolute_url)

    return links

if __name__ == "__main__":
    url_to_crawl = input("Enter the URL to crawl: ")
    crawled_links = get_all_links(url_to_crawl)
    with open('links_without_selenium.txt','w') as fh:
        fh.write('\n'.join(crawled_links))
    print(crawled_links)
