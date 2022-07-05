from selenium import webdriver
import time
tank = 'tank:10'
value = 50

navegador = './chromedriver.exe'
url='https://mypid.smartpid.com/mypid/'

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

time.sleep(1)

driver.refresh()

time.sleep(5)

if tank == 'tank:3':
    driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
    #driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
    #driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
    #time.sleep(3)
    #driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
if tank == 'tank:4':
    driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
    driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
    #driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
    #driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
    #time.sleep(3)
    #driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
if tank == 'tank:5':
    driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
   # driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
    #time.sleep(3)
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
if tank == 'tank:6':
    driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
    driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
    #time.sleep(3)
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
if tank == 'tank:7':
    driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
    #time.sleep(3)
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
if tank == 'tank:8':
    driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
    driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
    #time.sleep(3)
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
if tank == 'tank:9':
    driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
    #time.sleep(3)
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
if tank == 'tank:10':
    driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
    driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
    #time.sleep(3)
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
    #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()

