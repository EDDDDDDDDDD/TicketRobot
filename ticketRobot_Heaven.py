from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


chromedriver = "./chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.set_window_size(1300, 1200)
# Which website?
driver.get('https://www.feastogether.com.tw/booking/1')

locator = (By.XPATH, "//*[@id=\"modal-news\"]/div/div/div/button")
 
search = WebDriverWait(driver, 10).until(
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
people.send_keys("12") # How many people

ActionChains(driver).move_by_offset(200, 100).click().perform()
locator = (By.LINK_TEXT, "我知道了")
search = WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable(locator)
)
driver.find_element("link text", '我知道了').click()



# Date
driver.find_element("xpath", '/html/body/div[4]/div/div/div/ul/li[3]/div/input').click()
locator = (By.XPATH, "/html/body/div[14]/div[1]/span[3]")
search = WebDriverWait(driver, 10).until(
	EC.visibility_of_element_located(locator)
)
driver.find_element(By.XPATH, '/html/body/div[14]/div[1]/span[2]/span').click()
date = driver.find_element(By.XPATH, './/*[@class = \'flatpickr-day nextMonthDay\' and contains(text(),\'1\')]').click()

# luch, Afternoon-tea, Dinner
driver.find_element(By.XPATH, './/*[@class = \'wk-type-dinner\']').click() # Dinner
                        # LUNCH:         wk-type-lunch
                        # AFTERNOON_TEA: wk-type-afternoon-tea

# Wait for Search Result
"""
locator = (By.XPATH, ".//*[@class=\'wk-meal-times-search relative active\']")
search = WebDriverWait(driver, 10).until(
	EC.visibility_of_element_located(locator)
)
"""

driver.find_element(By.XPATH, '//*[@id=\"select_store\"]').click()
ActionChains(driver).scroll_by_amount(0, 300).perform()
locator = (By.XPATH, ".//*[@rel=\"大直店\"]")
search = WebDriverWait(driver, 10).until(
	EC.visibility_of_element_located(locator)
)
driver.find_element(By.XPATH, './/*[@rel=\"大直店\"]').click() # Store Name
ActionChains(driver).scroll_by_amount(0, 200).perform()
driver.find_element(By.XPATH, './/*[@data-col-date=\'2022-09-05\']').click() # Change date YYYY-MM-DD

# When is the meal?
locator = (By.XPATH, "//*[@id=\"order_time\"]")
search = WebDriverWait(driver, 10).until(
	EC.visibility_of_element_located(locator)
)
driver.find_element(By.XPATH, '//*[@id=\"order_time\"]').click()
select = Select(driver.find_element(By.XPATH, '//*[@id=\"order_time\"]'))
select.select_by_visible_text('18:30') # Choose what time



# COMFIRMED
submit = driver.find_element(By.XPATH, './/*[@type=\'button\' and contains(text(), \'確認訂位\')]')
ActionChains(driver).scroll_by_amount(0, 500).perform()
ActionChains(driver).move_to_element(submit).click(submit).perform()


print("COMPLETED!")

"""
locator = (By.LINK_TEXT, "分桌")
search = WebDriverWait(driver, 10).until(
	EC.visibility_of_element_located(locator)
)
driver.find_element("link text", '我知道了').click()
date = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/ul/li[3]/div/input")
"""
