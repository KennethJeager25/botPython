from selenium import webdriver
import time
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By

navegador = './chromedriver.exe'
url='https://mypid.smartpid.com/mypid/'

keyboard = Controller()

driver = webdriver.Chrome(navegador)
driver.get(url)

driver.find_element_by_xpath('//*[@id="sign-in-container"]/ion-grid/ion-row[1]/ion-col/ion-list/ion-item[1]/ion-input/input').send_keys('marrito@me.com')
driver.find_element_by_xpath('//*[@id="sign-in-container"]/ion-grid/ion-row[1]/ion-col/ion-list/ion-item[2]/ion-input/input').send_keys('goodbeer#2022')
driver.find_element_by_xpath('//*[@id="sign-in-container"]/ion-grid/ion-row[2]/ion-col/ion-button').click()


driver.refresh()

driver.execute_script("window.localStorage.setItem('EMAIL', 'marrito@me.com')")
driver.execute_script("window.sessionStorage.setItem('MY_PASSWORD', 'goodbeer#2022')")
driver.execute_script("window.sessionStorage.setItem('MY_SESSION', 'ALREADY_PRESENT')")

driver.get('https://mypid.smartpid.com/mypid/dashboard')

driver.maximize_window()

driver.refresh()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


