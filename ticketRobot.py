import time
from threading import Timer
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Information:
    def __init__(self, website, group, type, storeName, date, mealTime):
        self.website = website
        self.group = group
        self.type = self.getType(type)
        self.storeName = storeName
        self.date = date
        self.mealTime = mealTime
        
    def getType(self, type):
        if( type == "Dinner" ):
            return "wk-type-dinner"
        elif( type == "Lunch" ):
            return "wk-type-lunch"
        elif( type == "Aftertea" ):
            return "wk-type-afternoon-te"

class StartTime:
    def __init__(self, nextDays, hr, min, sec, microsec):
        self.nextDays = nextDays
        self.hr = hr
        self.min = min
        self.sec = sec
        self.microsec = microsec
    
    def exe(self, info):
        x = datetime.today()
        y = x.replace(day=x.day, \
                      hour=self.hr, \
                      minute=self.min, \
                      second=self.sec, \
                      microsecond=self.microsec) + \
                    timedelta(days=self.nextDays)
        delta_t = y-x

        secs = delta_t.total_seconds()
        print("Start in", secs, "secs.")
        robot = TicketRobot(info)
        t = Timer(secs, robot.robTicket)
        t.start()
        
        time.sleep(60)

class TicketRobot:
    def __init__(self, info):
        self.info = info
        
    def robTicket(self):
        chromedriver = "./chromedriver"
        driver = webdriver.Chrome(chromedriver)
        driver.set_window_size(1300, 1200)
        
        # Which website?
        driver.get(self.info.website)
        
        locator = (By.XPATH, "//*[@id=\"modal-news\"]/div/div/div/button")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
    
        driver.find_element("link text", '我知道了').click()
    
        # Loging
        driver.find_element(By.XPATH, "//*[@id=\"header\"]/div[2]/div/ul/li[2]/p").click()
        account = driver.find_element(By.XPATH, "//*[@id=\"form-login-header\"]/ul/li[1]/input")
        account.send_keys("0975307222")
        password = driver.find_element(By.XPATH, "//*[@id=\"form-login-header\"]/ul/li[2]/input")
        password.send_keys("giveme7788")
        driver.find_element(By.XPATH, "//*[@id=\"form-login-header\"]/ul/li[4]/button").click()
        WebDriverWait(driver, 10).until(
            EC.alert_is_present()
        )
        alert = driver.switch_to.alert
        alert.accept()
    
        # Number of the Group
        people = driver.find_element(By.XPATH, "//*[@id=\"book_people\"]")
        people.send_keys(self.info.group) # How many people
    
        ActionChains(driver).move_by_offset(200, 100).click().perform()
        locator = (By.LINK_TEXT, "我知道了")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        driver.find_element("link text", '我知道了').click()
    
        # Date
        driver.find_element("xpath", '/html/body/div[4]/div/div/div/ul/li[3]/div/input').click()
        locator = (By.XPATH, "/html/body/div[14]/div[1]/span[3]")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        driver.find_element(By.XPATH, '/html/body/div[14]/div[1]/span[2]/span').click()
        driver.find_element(By.XPATH, './/*[@class = \'flatpickr-day nextMonthDay\' and contains(text(),\'1\')]').click()
    
        # Type: luch, Afternoon-tea, Dinner
        typeXPATH = './/*[@class = \''+ self.info.type +'\']'
        driver.find_element(By.XPATH, typeXPATH).click() 
                                # Dinner:        wk-type-dinner
                                # LUNCH:         wk-type-lunch
                                # AFTERNOON_TEA: wk-type-afternoon-tea
    
        # Wait for Search Result
        """
        locator = (By.XPATH, ".//*[@class=\'wk-meal-times-search relative active\']")
        search = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        """
        storeXPATH = './/*[@rel=\''+ self.info.storeName +'\']'
        driver.find_element(By.XPATH, '//*[@id=\"select_store\"]').click()
        ActionChains(driver).scroll_by_amount(0, 300).perform()
        locator = (By.XPATH, storeXPATH)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        
        driver.find_element(By.XPATH, storeXPATH).click() # Store Name
        ActionChains(driver).scroll_by_amount(0, 200).perform()
        dateXPATH = './/*[@data-col-date=\''+ self.info.date +'\']'
        driver.find_element(By.XPATH, dateXPATH).click() # Change date YYYY-MM-DD
    
        # When is the meal?
        locator = (By.XPATH, "//*[@id=\"order_time\"]")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        driver.find_element(By.XPATH, '//*[@id=\"order_time\"]').click()
        select = Select(driver.find_element(By.XPATH, '//*[@id=\"order_time\"]'))
        select.select_by_visible_text(self.info.mealTime) # Choose what time
    
        # COMFIRMED
        submit = driver.find_element(By.XPATH, './/*[@type=\'button\' and contains(text(), \'確認訂位\')]')
        ActionChains(driver).scroll_by_amount(0, 500).perform()
        ActionChains(driver).move_to_element(submit).click(submit).perform()
        locator = (By.LINK_TEXT, "立即下載")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        driver.find_element("link text", '立即下載').click()
        
        print("COMPLETED!")
        time.sleep(3600)

    
def main():
    sunriseSite = "https://www.feastogether.com.tw/booking/10"
    heavenSite  = "https://www.feastogether.com.tw/booking/1"
    
    # Website to go
    # How many people?
    # Three Types: Dinner, Lunch, Aftertea
    # Store Name
    # Date
    # Mealtime
    sunrise = Information(sunriseSite, \
                            "12", \
                            "Dinner", \
                            "旭集信義店", \
                            "2022-09-06", \
                            "18:30")
    heaven  = Information(heavenSite, \
                            "12", \
                            "Dinner", \
                            "大直店", \
                            "2022-09-06", \
                            "18:30")
                    
    start = StartTime(0, 19, 00, 30, 0)  #nextDays, hr, min, sec, msec
    start.exe(heaven)
    
if __name__ == '__main__':
    main()
