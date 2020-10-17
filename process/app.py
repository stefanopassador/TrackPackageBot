from time import sleep
from scraper import scraper, upsscraper


    
    

if __name__ == '__main__':
    ups = upsscraper.UPSScraper()
    print(ups.scrape("1Z3746A36802537112%0D%0A"))
