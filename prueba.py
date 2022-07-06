from selenium import webdriver
import time

navegador = './chromedriver.exe'
url='https://www.programiz.com/python-programming/methods/string/split'


driver = webdriver.Chrome(navegador)
driver.get(url)

driver.execute_script("window.scrollBy(0,1000)","")