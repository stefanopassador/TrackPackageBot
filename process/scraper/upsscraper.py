from scraper.scraper import Scraper

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class UPSScraper(Scraper):
    def scrape(self, track_number):
        driver = self.driver
        
        url = "https://www.ups.com/track?loc=it_IT&tracknum=" + track_number + "&requester=WT/trackdetails"
        
        driver.get(url)

        # Accept all cookies and press the continue button
        driver.implicitly_wait(5)
        print('Stop waiting implicitly, now ok to Cookies')

        radio_button = driver.find_element_by_id('privacy_pref_optin')
        cookie_ok_button = driver.find_element_by_id('consent_prompt_submit')
        
        ActionChains(driver).move_to_element(radio_button).perform()
        ActionChains(driver).click(radio_button).perform()
        ActionChains(driver).move_to_element(cookie_ok_button)
        ActionChains(driver).click(cookie_ok_button).perform()
        print('Cookies accepted, now waiting...')

        # Read status
        driver.implicitly_wait(10)
        print('Stop waiting implicitly')

        driver.find_element_by_tag_name('ups-shipment-progress').find_element_by_tag_name('tbody')
        last_update = driver.find_element_by_id('stApp_ShpmtProg_LVP_progress_row_1')
        last_update_datetime = last_update.find_element_by_id('stApp_ShpmtProg_LVP_milestone_1_DateTime_1')
        last_update_date = last_update_datetime.find_element_by_id('stApp_ShpmtProg_LVP_milestone_1_date_1').text
        last_update_time = last_update.find_element_by_id('stApp_ShpmtProg_LVP_milestone_1_time_1').text
        last_update_locality = last_update.find_element_by_id('stApp_ShpmtProg_LVP_milestone_1_location_1').find_element_by_tag_name('span').text

        driver.close()

        print('Last update on {}, the package was at {}'.format(last_update_date+' '+last_update_time, last_update_locality))
        
        d = dict()
        d['timestamp'] = last_update_date+' '+last_update_time
        d['location'] = last_update_locality
        return d