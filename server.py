from selenium import webdriver
import time
from classTempCH1 import temp_CH1
from classTempCH2 import temp_CH2
from pynput.keyboard import Key, Controller

keyboard = Controller()
tank = 'tank:8'
value = 50

class Bot:

    def __init__(self,url='',navegador=''):
        self.url = url
        self.navegador = navegador
        self.ch1 = temp_CH1()
        self.ch2 = temp_CH2()
        

    def setTemp(self):
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

        if tank == 'tank:3':
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        if tank == 'tank:4':
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        if tank == 'tank:5':
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        if tank == 'tank:6':
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        if tank == 'tank:7':
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        if tank == 'tank:8':
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            #driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        if tank == 'tank:9':
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[1]/ion-item/ion-input/input').send_keys(value)
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[2]/div[1]/ion-card[1]/ion-grid/ion-row[2]/ion-col[3]/ion-button/small').click()
            driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        if tank == 'tank:10':
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
        tempCH1tank3 = temp_CH1()
        tempCH1tank3.name = 'Tank:3'
        tempCH1tank3.value = tank3[0]
        self.ch1.addCh1(tempCH1tank3)
        tank = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[2]/ion-col[1]/div[1]/ion-label")
        tank5 = tank.text.split('°')
        tempCH1tank5 = temp_CH1()
        tempCH1tank5.name = 'Tank:5'
        tempCH1tank5.value = tank5[0]
        self.ch1.addCh1(tempCH1tank5)
        driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[1]').click()
        driver.find_element_by_xpath('//*[@id="myFixZone"]/ion-card-header/ion-toolbar/ion-buttons[1]/ion-button[3]').click()
        self.scrolldown()
        time.sleep(3)
        tank = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[2]/ion-col[1]/div[1]/ion-label")
        tank7 = tank.text.split('°')
        tempCH1tank7 = temp_CH1()
        tempCH1tank7.name = 'Tank:7'
        tempCH1tank7.value = tank7[0]
        self.ch1.addCh1(tempCH1tank7)
        tank = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[2]/ion-col[1]/div[1]/ion-label")
        tank9 = tank.text.split('°')
        tempCH1tank9 = temp_CH1()
        tempCH1tank9.name = 'Tank:9'
        tempCH1tank9.value = tank9[0]
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
        tempCH1tank4 = temp_CH2()
        tempCH1tank4.name = 'Tank:4'
        tempCH1tank4.value = tank4[0]
        self.ch2.addCh2(tempCH1tank4)
        driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
        tank = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[2]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[2]/ion-col[1]/div[2]/ion-label")
        tank6 = tank.text.split('°')
        tempCH1tank6 = temp_CH2()
        tempCH1tank6.name = 'Tank:6'
        tempCH1tank6.value = tank6[0]
        self.ch2.addCh2(tempCH1tank6)
        self.scrolldown()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
        tank = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[2]/ion-col[1]/div[2]/ion-label")
        tank8 = tank.text.split('°')
        tempCH1tank8 = temp_CH2()
        tempCH1tank8.name = 'Tank:8'
        tempCH1tank8.value = tank8[0]
        self.ch2.addCh2(tempCH1tank8)
        driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
        tank = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[4]/ion-card/div[1]/ion-card-content/div[1]/div[1]/ion-card/ion-row[2]/ion-col[1]/div[2]/ion-label")
        tank10 = tank.text.split('°')
        tempCH1tank10 = temp_CH2()
        tempCH1tank10.name = 'Tank:10'
        tempCH1tank10.value = tank10[0]
        self.ch2.addCh2(tempCH1tank10)
        self.ch2.guardarDatos()

    def showSpTempCH1(self):
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

        



    def scrolldown(self):
        for j in range(14):
            keyboard.press(Key.down)
            keyboard.release(Key.down)



if __name__ == '__main__':
    validacion = 2
    botsito = Bot()
    try:
        if validacion == 1:
            botsito.setTemp()
        else:
            botsito.showTempCH1()
            botsito.showTempCH2()
    except KeyboardInterrupt:
        print ('Fin del programa')