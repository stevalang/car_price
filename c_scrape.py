import requests
from bs4 import BeautifulSoup

# Get list of offers
URL = 'https://sfbay.craigslist.org/search/cta?query=tesla'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='rows')
car_elems = results.find_all('li', class_='result-row')

# Parse each offer tile
for car_elem in car_elems:
    price_elem = car_elem.find('span', class_='result-price')
    url_elem = car_elem.find('a', class_='result-image gallery')['href']
    title_elem = car_elem.find('a', class_='result-title hdrlnk')

    print(title_elem.text.strip())
    print(url_elem)
    print(price_elem.text.strip())
    print()

# Get details ofrticular offer
CAR_URL = 'https://sfbay.craigslist.org/pen/cto/d/burlingame-2017-tesla-x75d-ap2-seats/7293222826.html'
car_page = requests.get(CAR_URL)
car_soup = BeautifulSoup(car_page.content, 'html.parser')
attributes = car_soup.find_all('p', class_='attrgroup')

# Get attribures
for attribute in attributes:
    spans = attribute.find_all('span')
    for span in spans:
        text = span.text.strip()
        print(text)
        print(text.split(':'))
        print()

# Get offer description
posting_body = car_soup.find('section', {'id': 'postingbody'})
print(posting_body.text)

