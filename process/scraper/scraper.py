from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Scraper(object):
    def __init__(self):  
        CHROME_PATH = '/usr/bin/google-chrome'
        CHROMEDRIVER_PATH = './chromedriver.exe'
        WINDOW_SIZE = "1920,1080"

        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        #chrome_options.binary_location = CHROME_PATH

        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)  
        

    def scrape(self, track_number):
        print("There are many delivery currier, select one ;)")

        return None, None