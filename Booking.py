from selenium import webdriver
from selenium.webdriver.common.by import By
import const
import os
import time


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False, driver_path=r"./chromedriver.exe"):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def get_page(self):
        self.get(const.PAGE_URL)

    def select_place_to_go(self, place_to_go):
        searchbar = self.find_element(by=By.ID, value='ss')
        searchbar.click()
        searchbar.send_keys(place_to_go)
        time.sleep(1)
        first_result = self.find_element(by=By.CSS_SELECTOR, value='li[data-i="0"]')
        first_result.click()

    # year-month-day

    def select_dates(self, check_in_date, check_out_date):
        check_in = self.find_element(by=By.CSS_SELECTOR, value=f'td[data-date="{check_in_date}"]')
        check_in.click()
        check_out = self.find_element(by=By.CSS_SELECTOR, value=f'td[data-date="{check_out_date}"]')
        check_out.click()

    def num_of_people(self):
        self.find_element(by=By.ID, value='xp__guests__toggle').click()
        time.sleep(1)
        self.find_element(by=By.CSS_SELECTOR, value='button[aria-describedby="group_adults_desc"]').click()
        time.sleep(1)
        self.find_element(by=By.CSS_SELECTOR, value='button[type="submit"]').click()

    def paste_options_into_notepad(self):
        hotel_cards = self.find_elements(by=By.CLASS_NAME, value='c90a25d457')
        links = [hotel_card.find_element(by=By.CSS_SELECTOR, value='a').get_attribute('href') for hotel_card in hotel_cards]
        with open('hotels.txt', 'w') as notepad:
            print(*links, file=notepad, sep='\n')
            self.close()

