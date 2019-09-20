import random
import sys

try:
    from bs4 import BeautifulSoup
    import requests
except ImportError:
    print("Please run 'pip install -r requirements.txt'")
    sys.exit(1)

BEYOGLU_URL = 'https://www.zingat.com/beyoglu-bolge-raporu'
KADIKOY_URL = 'https://www.zingat.com/kadikoy-bolge-raporu'

USER_AGENT_LIST = [
    #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

def parse_page(url):
    """Open and parse page content

    :type url: str
    :param url: url of the page to be parsed
    :rtype: BeautifulSoup
    :returns: BeautifulSoup object
    """

    print(f'\n*** Parsing url: {url} ...')

    # pick a random user agent
    user_agent = random.choice(USER_AGENT_LIST)

    # set header
    headers = {'User-Agent': user_agent}

    response = requests.get(url, headers=headers)
    print('*** Response status:', response.status_code)
    parsed_page = BeautifulSoup(response.content, "lxml")

    return parsed_page


def get_avg_rent_for_borough(url):

    parsed_page = parse_page(url)

    rent_price_container = parsed_page.find("div", {'data-zingalite': 'marketPrice-rent'})

    avg_rent_price = rent_price_container.select('p')[1].text.split()[0]

    print(f"Avg. Rent Price for {url.split('/')[-1].split('-')[0].upper()}: {avg_rent_price}")

    return float(avg_rent_price)


def get_average_prices():

    urls = (BEYOGLU_URL, KADIKOY_URL)

    avg_prices = []

    for url in urls:
        avg_prices.append(get_avg_rent_for_borough(url))

    return avg_prices


def main():
    """Entry point for the program"""

    get_average_prices()



if __name__ == '__main__':

    main()

