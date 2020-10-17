from bs4 import BeautifulSoup
import requests

def scraping():
    track_number = "1Z3746A36802537112%0D%0A"
    url = "https://www.ups.com/track?loc=it_IT&tracknum= " + track_number + "&requester=WT/trackdetails"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    print(soup.prettify())

if __name__ == '__main__':
    scraping()