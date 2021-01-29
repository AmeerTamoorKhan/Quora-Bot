from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import numpy as np
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context


class AskMe:

    def __init__(self, search):
        self.search = search
        self.answer = []
        self.init_driver()
        self.wait = WebDriverWait(self.driver, 20)
        self.login()
        self.search_question()
        self.grab_answer()

    def init_driver(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path="Driver/chromedriver", options=self.options)
        self.pinterest= self.driver.get('https://www.quora.com/')

    def login(self):
        #time.sleep(10)
        username = 'khanameerkhan1994@gmail.com'
        password = 'Allahis1'
        try:
            # Enter your username
            self.wait.until(ec.element_to_be_clickable((By.XPATH, '//input[@placeholder="Email"]'))).send_keys(username)
            # Enter your password
            self.wait.until(ec.element_to_be_clickable((By.XPATH, '//input[@placeholder="Password"]'))).send_keys(password)
            # Click the login button
            self.wait.until(ec.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Login"]'))).click()
        except TimeoutException:
            pass

    def search_question(self):
        # Enter your search in the search box
        self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[2]/form/div/div/div/div/div/input'))).send_keys(self.search)
        # Press Enter to find the required search
        time.sleep(5)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[2]/form/div/div/div[2]/div/div[2]/div'))).click()

    def grab_answer(self):
        #time.sleep(5)
        # Find all the relevant comments from the page
        self.wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div/div[1]/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]'))).click()
        #element.click()
        time.sleep(5)
        print('Hello')
        #self.driver.switch_to.window(self.driver.window_handles[1])
        parent_nodes = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div/div[1]/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]')
        self.answer = parent_nodes.text
        # counts = []
        # for parent_node in parent_nodes:
        #     try:
        #         print('Hello1')
        #         upvote = parent_node.find_element_by_xpath('.//span[@name="Upvote"]/../div//span')
        #         if upvote.text[-1].isdigit():
        #             print(upvote.text[-1])
        #             counts.append(float(upvote.text))
        #             print(float(upvote.text))
        #         else:
        #             print(upvote.text[-1])
        #             counts.append(float(upvote.text[:-1]))
        #             print(float(upvote.text[:-1]))
        #     except NoSuchElementException:
        #         pass
        #
        # max_upvotes_ind = max(counts)
        #
        # # Open the best comment in new window by clicking
        # time.sleep(1)
        # for parent_node in parent_nodes:
        #     try:
        #         upvote = parent_node.find_element_by_xpath('.//span[@name="Upvote"]/../div//span')
        #         if upvote.text[-1].isdigit():
        #             upvote = float(upvote.text)
        #         else:
        #             upvote = float(upvote.text[:-1])
        #
        #         if upvote == max_upvotes_ind:
        #             comment = parent_node.find_element_by_xpath('.//div[@class="q-relative spacing_log_answer_content"]')
        #             comment.click()
        #             # Grab the best comment from the new window
        #             self.answer = comment.text
        #             break
        #     except (NoSuchElementException, TimeoutException):
        #         pass

        self.driver.quit()


if __name__ == "__main__":
    pass