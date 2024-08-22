from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tabulate import tabulate
import datetime

with open('quantities.txt', "r") as file:
    qtys = file.readlines()
    qtys = [qty.strip() for qty in qtys]

with open('postcodes.txt', "r") as file:
    postcodes = file.readlines()
    postcodes = [postcode.strip().split(':') for postcode in postcodes]


link = 'https://www.onlineturf.co.uk/products/turf/budget'
options = webdriver.FirefoxOptions()
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)
driver.get(link)

qty_input = driver.find_element(By.ID, "qty")
postcode_input = driver.find_element(By.ID, "postcode")
calculate_button = driver.find_element(By.XPATH, "//button[@type='submit']")
#calculate_button = driver.find_element(By.CLASS_NAME, "btn-primary")

budgetPrices = []

for postcode in postcodes:
    prices=[postcode[0]]
    for qty in qtys:

        qty_input.clear()
        postcode_input.clear()

        qty_input.send_keys(qty)
        postcode_input.send_keys(postcode[1])

        calculate_button.click()

        time.sleep(0.5)

        total = driver.find_element(By.XPATH, "//td[@data-id='total']")
        prices.append(total.text[1:])
    budgetPrices.append(prices)
# driver.quit()
print(tabulate(budgetPrices, headers=['BUDGET']+qtys))
print()


link = 'https://www.onlineturf.co.uk/products/turf/stadium'
# options = webdriver.FirefoxOptions()
# options.add_argument("-headless")
# driver = webdriver.Firefox(options=options)
driver.get(link)

qty_input = driver.find_element(By.ID, "qty")
postcode_input = driver.find_element(By.ID, "postcode")
calculate_button = driver.find_element(By.XPATH, "//button[@type='submit']")
#calculate_button = driver.find_element(By.CLASS_NAME, "btn-primary")

stadiumPrices = []

for postcode in postcodes:
    prices=[postcode[0]]
    for qty in qtys:

        qty_input.clear()
        postcode_input.clear()

        qty_input.send_keys(qty)
        postcode_input.send_keys(postcode[1])

        calculate_button.click()

        time.sleep(0.5)

        total = driver.find_element(By.XPATH, "//td[@data-id='total']")
        prices.append(total.text[1:])
    stadiumPrices.append(prices)
# driver.quit()
print(tabulate(stadiumPrices, headers=['STADIUM']+qtys))
print()


link = 'https://www.onlineturf.co.uk/products/turf/rye-gold'
# options = webdriver.FirefoxOptions()
# options.add_argument("-headless")
# driver = webdriver.Firefox(options=options)
driver.get(link)

qty_input = driver.find_element(By.ID, "qty")
postcode_input = driver.find_element(By.ID, "postcode")
calculate_button = driver.find_element(By.XPATH, "//button[@type='submit']")
# calculate_button = driver.find_element(By.CLASS_NAME, "btn-primary")

ryePrices = []

for postcode in postcodes:
    prices=[postcode[0]]
    for qty in qtys:

        qty_input.clear()
        postcode_input.clear()

        qty_input.send_keys(qty)
        postcode_input.send_keys(postcode[1])

        calculate_button.click()

        time.sleep(0.5)

        total = driver.find_element(By.XPATH, "//td[@data-id='total']")
        prices.append(total.text[1:])
    ryePrices.append(prices)
driver.quit()
print(tabulate(ryePrices, headers=['RYE-GOLD']+qtys))

current_date = datetime.date.today()
formatted_date = current_date.strftime("%Y-%m-%d")

with open('prices-'+formatted_date+'.txt', 'w') as file:
    file.write(tabulate(budgetPrices, headers=['Budget']+qtys))
    file.write('\n\n\n')
    file.write(tabulate(stadiumPrices, headers=['Stadium']+qtys))
    file.write('\n\n\n')
    file.write(tabulate(ryePrices, headers=['Rye-Gold']+qtys))