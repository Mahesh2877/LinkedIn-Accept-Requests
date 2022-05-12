from IPython import display
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from selenium.webdriver import ActionChains

# Ask the user for the username and password.
# getpass() ensures that the password will not be visible during input
USERNAME = input("Enter the username: ")
PASSWORD = getpass("Enter the password: ")

# Load the Chrome browser before openning it
driver = webdriver.Chrome(ChromeDriverManager().install())

# Visit the url showing the list of connection requests
driver.get('https://www.linkedin.com/mynetwork/invitation-manager/')

# Maximize the browser window
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

# First sleep for a while to give time for the elements to load...
# ...If we don't sleep, I've noticed that the code fails in the following line
# Find & Click on the "people" button to go to list of people's requests
sleep(5)
people_button = driver.find_element_by_id("mn-invitation-manager__invitation-facet-pills--CONNECTION")
people_button.click()

# Use xpath to find the list of Accept buttons to Click
# The syntax in this line basically says to look for the <button> tag first...
# ...then find the "class" attribute having the exact same value as given here
sleep(5)
accept_buttons = driver.find_elements_by_xpath("//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view invitation-card__action-btn']")
# Iterate through the list of buttons and start CLICKING 'EM!!!'
for individual_button in accept_buttons:
    individual_button.click()

# Sleep for a while before closing the window
sleep(5)
driver.close()
