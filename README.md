# TicketRobot
### Python Version: 3.10.5
### Selenium Version: 4.3.0
### Author: Edward


## Python program to rob tickets legally

#### Step 1. Download and install Python (Python 3.10.5 Windows installer 64-bit)
https://www.python.org/downloads/windows/


#### Step 2. Install Selenium (PowerShell)

    $ pip install selenium


Line 14: driver.get('WEBSITE')

Line 40: people.send_keys("How many people")

Line 61: driver.find_element(By.XPATH, './/*[@class = \'WHICH_ONE\']').click() 
                        
    # LUNCH:         wk-type-lunch
    # AFTERNOON_TEA: wk-type-afternoon-tea
    # Dinner:        wk-type-dinner
                        
Line 74: driver.find_element(By.XPATH, './/*[@rel=\"STORE_NAME\"]').click()

Line 76: driver.find_element(By.XPATH, './/*[@data-col-date=\'DATE\']').click()
                                                            
     # YYYY-MM-DD
                                                            
Line 85: select.select_by_visible_text('WHAT_TIME')
