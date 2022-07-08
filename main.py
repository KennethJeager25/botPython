from selenium import webdriver
import time
from classTempCH1 import temp_CH1
from classTempCH2 import temp_CH2
from classApi import Api
from pynput.keyboard import Key, Controller

keyboard = Controller()

class Bot:

    def __init__(self,url='',navegador=''):
        self.url = url
        self.navegador = navegador
        self.ch1 = temp_CH1()
        self.ch2 = temp_CH2()
        self.api = Api()
        

    def setTemp(self,tank,value):
        self.navegador = './chromedriver.exe'
        self.url='https://mypid.smartpid.com/mypid/'

        driver = webdriver.Chrome(self.navegador)
        driver.get(self.url)

        driver.find_element_by_xpath('//*[@id="sign-in-container"]/ion-grid/ion-row[1]/ion-col/ion-list/ion-item[1]/ion-input/input').send_keys('marrito@me.com')
        driver.find_element_by_xpath('//*[@id="sign-in-container"]/ion-grid/ion-row[1]/ion-col/ion-list/ion-item[2]/ion-input/input').send_keys('goodbeer#2022')
        driver.find_element_by_xpath('//*[@id="sign-in-container"]/ion-grid/ion-row[2]/ion-col/ion-button').click()

        self.url='https://mypid.smartpid.com/mypid/dashboard'
        driver.refresh()

        driver.execute_script("window.localStorage.setItem('EMAIL', 'marrito@me.com')")
        driver.execute_script("window.sessionStorage.setItem('MY_PASSWORD', 'goodbeer#2022')")
        driver.execute_script("window.sessionStorage.setItem('MY_SESSION', 'ALREADY_PRESENT')")

        driver.get(self.url)

        time.sleep(1)

        driver.refresh()

        time.sleep(5)

        if tank == 'Tank 3':
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        if tank == 'Tank 4':
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        if tank == 'Tank 5':
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        if tank == 'Tank 6':
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        if tank == 'Tank 7':
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
            self.scrolldown()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        if tank == 'Tank 8':
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
            self.scrolldown()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        if tank == 'Tank 9':
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
            self.scrolldown()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        if tank == 'Tank 10':
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
            self.scrolldown()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()

    def showTempCH1(self):
        self.navegador = './chromedriver.exe'
        self.url='https://mypid.smartpid.com/mypid/'

        driver = webdriver.Chrome(self.navegador)
        driver.get(self.url)

        driver.find_element_by_xpath('//*[@id="sign-in-container"]/ion-grid/ion-row[1]/ion-col/ion-list/ion-item[1]/ion-input/input').send_keys('marrito@me.com')
        driver.find_element_by_xpath('//*[@id="sign-in-container"]/ion-grid/ion-row[1]/ion-col/ion-list/ion-item[2]/ion-input/input').send_keys('goodbeer#2022')
        driver.find_element_by_xpath('//*[@id="sign-in-container"]/ion-grid/ion-row[2]/ion-col/ion-button').click()

        self.url='https://mypid.smartpid.com/mypid/dashboard'
        driver.refresh()

        driver.execute_script("window.localStorage.setItem('EMAIL', 'marrito@me.com')")
        driver.execute_script("window.sessionStorage.setItem('MY_PASSWORD', 'goodbeer#2022')")
        driver.execute_script("window.sessionStorage.setItem('MY_SESSION', 'ALREADY_PRESENT')")

        driver.get(self.url)

        driver.refresh()

        time.sleep(9)

        tank = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[1]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[2]/ion-col[1]/div[1]/ion-label")
        tank3 = tank.text.split('°')
        tanksp = driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-content/div[1]/div[1]/ion-card/ion-row[4]/ion-col[1]/div[1]/ion-label')
        tankSp3 = tanksp.text.split('°')
        tempCH1tank3 = temp_CH1()
        tempCH1tank3.name = 'Tank 3'
        tempCH1tank3.value = tank3[0]
        tempCH1tank3.sp = tankSp3[0]
        self.ch1.addCh1(tempCH1tank3)
        tank = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[2]/ion-col[1]/div[1]/ion-label")
        tank5 = tank.text.split('°')
        tanksp = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[4]/ion-col[1]/div[1]/ion-label')
        tankSp5 = tanksp.text.split('°')
        tempCH1tank5 = temp_CH1()
        tempCH1tank5.name = 'Tank 5'
        tempCH1tank5.value = tank5[0]
        tempCH1tank5.sp = tankSp5[0]
        self.ch1.addCh1(tempCH1tank5)
        driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
        driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        self.scrolldown()
        time.sleep(5)
        tank = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[2]/ion-col[1]/div[1]/ion-label")
        tank7 = tank.text.split('°')
        tanksp = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[4]/ion-col[1]/div[1]/ion-label')
        tankSp7 = tanksp.text.split('°')
        tempCH1tank7 = temp_CH1()
        tempCH1tank7.name = 'Tank 7'
        tempCH1tank7.value = tank7[0]
        tempCH1tank7.sp = tankSp7[0]
        self.ch1.addCh1(tempCH1tank7)
        tank = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[2]/ion-col[1]/div[1]/ion-label")
        tank9 = tank.text.split('°')
        tanksp = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[4]/ion-col[1]/div[1]/ion-label')
        tankSp9 = tanksp.text.split('°')
        tempCH1tank9 = temp_CH1()
        tempCH1tank9.name = 'Tank 9'
        tempCH1tank9.value = tank9[0]
        tempCH1tank9.sp = tankSp9[0]
        self.ch1.addCh1(tempCH1tank9)
        self.ch1.guardarDatos()
        time.sleep(3)

    def showTempCH2(self):
        self.navegador = './chromedriver.exe'
        self.url='https://mypid.smartpid.com/mypid/'

        driver = webdriver.Chrome(self.navegador)
        driver.get(self.url)

        driver.find_element_by_xpath('//*[@id="sign-in-container"]/ion-grid/ion-row[1]/ion-col/ion-list/ion-item[1]/ion-input/input').send_keys('marrito@me.com')
        driver.find_element_by_xpath('//*[@id="sign-in-container"]/ion-grid/ion-row[1]/ion-col/ion-list/ion-item[2]/ion-input/input').send_keys('goodbeer#2022')
        driver.find_element_by_xpath('//*[@id="sign-in-container"]/ion-grid/ion-row[2]/ion-col/ion-button').click()

        self.url='https://mypid.smartpid.com/mypid/dashboard'
        driver.refresh()

        driver.execute_script("window.localStorage.setItem('EMAIL', 'marrito@me.com')")
        driver.execute_script("window.sessionStorage.setItem('MY_PASSWORD', 'goodbeer#2022')")
        driver.execute_script("window.sessionStorage.setItem('MY_SESSION', 'ALREADY_PRESENT')")

        driver.get(self.url)

        time.sleep(9)

        driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
        tank = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[1]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[2]/ion-col[1]/div[2]/ion-label")
        tank4 = tank.text.split('°')
        tanksp = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[1]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[4]/ion-col[1]/div[2]/ion-label")
        tanksp4 = tanksp.text.split('°')
        tempCH2tank4 = temp_CH2()
        tempCH2tank4.name = 'Tank 4'
        tempCH2tank4.value = tank4[0]
        tempCH2tank4.sp = tanksp4[0]
        self.ch2.addCh2(tempCH2tank4)
        driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
        tank = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[2]/ion-col[1]/div[2]/ion-label")
        tank6 = tank.text.split('°')
        tanksp = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[4]/ion-col[1]/div[2]/ion-label')
        tanksp6 = tanksp.text.split('°')
        tempCH2tank6 = temp_CH2()
        tempCH2tank6.name = 'Tank 6'
        tempCH2tank6.value = tank6[0]
        tempCH2tank6.sp = tanksp6[0]
        self.ch2.addCh2(tempCH2tank6)
        driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
        driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        self.scrolldown()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
        tank = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[2]/ion-col[1]/div[2]/ion-label")
        tank8 = tank.text.split('°')
        tanksp = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[4]/ion-col[1]/div[2]/ion-label')
        tanksp8 = tanksp.text.split('°')
        tempCH2tank8 = temp_CH2()
        tempCH2tank8.name = 'Tank 8'
        tempCH2tank8.value = tank8[0]
        tempCH2tank8.sp = tanksp8[0]
        self.ch2.addCh2(tempCH2tank8)
        driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
        tank = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[2]/ion-col[1]/div[2]/ion-label")
        tank10 = tank.text.split('°')
        tanksp = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[4]/ion-col[1]/div[2]/ion-label')
        tanksp10 = tanksp.text.split('°')
        tempCH2tank10 = temp_CH2()
        tempCH2tank10.name = 'Tank 10'
        tempCH2tank10.value = tank10[0]
        tempCH2tank10.sp = tanksp10[0]
        self.ch2.addCh2(tempCH2tank10)
        self.ch2.guardarDatos()

    def scrolldown(self):
        for j in range(14):
            keyboard.press(Key.down)
            keyboard.release(Key.down)

    def metodoApi(self):
        self.api.metodoDelete()
        self.ch1.ApiRequest()
        self.ch2.ApiRequest()

    def getstatus(self):
       prueba =  self.api.getstatus()
       return prueba

    def getTank(self):
        tank = ''
        for value in self.api.getUpdate():
            tank = value['name']
        return tank

    def gatValue(self):
        value = ''
        for item in self.api.getUpdate():
            value = item['sp']
        return value



if __name__ == '__main__':
    botsito = Bot()
    try:
        if botsito.getstatus() == 'true':
            botsito.setTemp(botsito.getTank(),botsito.gatValue())
            botsito.showTempCH1()
            botsito.showTempCH2()
            botsito.metodoApi()
        else:
            botsito.showTempCH1()
            botsito.showTempCH2()
            botsito.metodoApi()
    except KeyboardInterrupt:
        print ('Fin del programa')