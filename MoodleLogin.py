from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = '.\msedgedriver.exe'  # Download edge driver for your version and replace its path here
driver = webdriver.Edge(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")

username = input("Enter the username ")
password = input("Enter the password ")

user_box = driver.find_element_by_xpath('//*[@id="username"]')
pass_box = driver.find_element_by_xpath('//*[@id="password"]')
capt_box = driver.find_element_by_xpath('//*[@id="valuepkg3"]')
entr_but = driver.find_element_by_xpath('//*[@id="loginbtn"]')
captcha = driver.find_element_by_id("login").text
words = captcha.split()

user_box.send_keys(username)
pass_box.send_keys(password)
capt_box.send_keys(Keys.BACK_SPACE)

if words[7] == "subtract":
    capt_box.send_keys(int(words[8]) - int(words[10]))
elif words[7] == "add":
    capt_box.send_keys(int(words[8]) + int(words[10]))
elif words[8] == "first":
    capt_box.send_keys(int(words[10]))
elif words[8] == "second":
    capt_box.send_keys(int(words[12]))


entr_but.click()
