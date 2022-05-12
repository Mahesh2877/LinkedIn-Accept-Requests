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

# Visit the url showing the list of connection requests
driver.get('https://www.linkedin.com/mynetwork/invitation-manager/')

# to maximize the browser window
driver.maximize_window()

#Click on "Sign In"
sign_in_link = driver.find_element_by_class_name("main__sign-in-link")
sign_in_link.click()

# Enter the login credentials and hit ENTER
email=driver.find_element_by_id("username")
email.send_keys(USERNAME)

password=driver.find_element_by_id("password")
password.send_keys(PASSWORD)

password.send_keys(Keys.RETURN)

# Find & Click on the "people" button to go to list of people's requests
sleep(5)
people_button = driver.find_element_by_id("mn-invitation-manager__invitation-facet-pills--CONNECTION")
people_button.click()

# Extract the list of "Accept" buttons for display
sleep(5)
accept_buttons = driver.find_elements_by_class_name("artdeco-button artdeco-button--2 artdeco-button--secondary ember-view invitation-card__action-btn")
# display.display(len(accept_button))
for individual_button in accept_buttons:
    individual_button.click()

# Sleep for a while
sleep(10)

# driver.close()
