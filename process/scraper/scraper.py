from selenium import webdriver

class Scraper(object):
    def __init__(self):
        DRIVER_PATH = './chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    def scrape(self, track_number):
        print("There are many delivery currier, select one ;)")

        return None, None