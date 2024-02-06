import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

origin_url = input('Enter the url that you want to crawl: ')

#function to get all the links
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

domains_data = get_all_links(origin_url)
print(f'Here is the data, {domains_data}')