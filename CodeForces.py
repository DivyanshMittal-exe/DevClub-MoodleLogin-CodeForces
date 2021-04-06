
from string import ascii_lowercase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import sys

from selenium.common.exceptions import TimeoutException


PATH = '.\\msedgedriver.exe'
driver = webdriver.Edge(PATH)
name = sys.arg[1]

for con in ascii_lowercase:
    driver.get(f"https://codeforces.com/problemset/problem/{name}/{con}")
    try:
        checker = driver.find_element_by_class_name("message").is_displayed()
        if checker == True:
            break
        dirloc = ".\\"+name+"\\"+con
        os.makedirs(dirloc)
        driver.screenshot(dirloc + "\\problem.png")
        inputs = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(By.CLASS_NAME, "input"))
        outputs = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(By.CLASS_NAME, "output"))
        for i in range(0, len(inputs)):
            file = open(dirloc+"\\input"+str(i+1)+".txt", 'w')
            file.write(inputs[i].find_element_by_tag_name("pre").text)
            file.close()

            file = open(dirloc+"\\output"+str(i+1)+".txt", 'w')
            file.write(
                outputs[i].find_element_by_tag_name("pre").text)
            file.close()
    except:
        pass

