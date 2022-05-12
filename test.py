from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from selenium.webdriver import ActionChains

USERNAME = input("Enter the username: ")
PASSWORD = getpass("Enter the password: ")

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.linkedin.com/uas/login")

# to maximize the browser window
driver.maximize_window()

email=driver.find_element_by_id("username")
email.send_keys(USERNAME)
password=driver.find_element_by_id("password")
password.send_keys(PASSWORD)
sleep(5)
password.send_keys(Keys.RETURN)
print("Entered login credentials")

#get method to launch the URL
driver.get('https://www.linkedin.com/mynetwork/invitation-manager/')
print("Openned network lists!!!!")
#to refresh the browser
#driver.refresh()
sleep(5)

button = driver.find_element_by_xpath("//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view invitation-card__action-btn']")

button.click()

# identifying the link with the help of link text locator
#driver.find_element_by_link_text("Company").click()

sleep(10)

driver.close()
