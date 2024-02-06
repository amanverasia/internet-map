from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_links(url):
    # Set up the Chrome WebDriver
    chrome_options = Options()
    #chrome_options.add_argument('--headless')  # Run in headless mode (no GUI)
    service = ChromeService(executable_path='chromedriver.exe')  # Provide the path to your chromedriver executable
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        links = [urljoin(url, link['href']) for link in soup.find_all('a', href=True)]
    finally:
        driver.quit()

    return links

if __name__ == "__main__":
    url_to_crawl = input("Enter the URL to crawl: ")
    crawled_links = get_all_links(url_to_crawl)
    with open('links_with_selenium.txt','w') as fh:
        fh.write('\n'.join(crawled_links))
    print(crawled_links)
