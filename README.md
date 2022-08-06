# TicketRobot
### Python Version: 3.10.5
### Selenium Version: 4.3.0
### Author: Edward


## Python program to rob tickets legally

#### Step 1. Download and install Python (Python 3.10.5 Windows installer 64-bit)
https://www.python.org/downloads/windows/


#### Step 2. Install Selenium (PowerShell)

    $ pip install selenium
#### 
#### Information Format
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
