from selenium import webdriver
import dotenv
import os

dotenv.load_dotenv()

CODECHEF_USER = os.getenv('CODECHEFUSER')
CODECHEF_PASS = os.getenv('CODECHEFPASS')
PATH = "D:\Python\Selenium Testing\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# getting the code from the file
with open('./solution.cpp', 'r') as file:
    code = file.read()

# getting the program code
programcode = input("Enter Problem Code: ")

# getting the website
driver.get(f"https://www.codechef.com/submit/{programcode.upper()}")

# getting the username and password field
username = driver.find_element_by_id("edit-name")
password = driver.find_element_by_id("edit-pass")

# sending the username and password to the fields
username.send_keys(CODECHEF_USER)
password.send_keys(CODECHEF_PASS)

# clicking on the Login Button
loginButton = driver.find_element_by_id('edit-submit')
loginButton.click()

try:
    textArea = driver.find_element_by_id("edit-program")
    textArea.send_keys(code)
except:
    ideButton = driver.find_element_by_id("edit-submit")
    ideButton.click()
    driver.implicitly_wait(5)
    textArea = driver.find_element_by_id("edit-program")
    textArea.send_keys(code)


# selecting language as C++14
driver.find_element_by_xpath("//*[@id='edit-language']/option[1]").click()

# finally submitting the solution to the codechef
driver.find_element_by_id("edit-submit-1").click()

# closing the driver
driver.close()
