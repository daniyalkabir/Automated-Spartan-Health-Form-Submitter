#DANIYAL KABIR DAR
# 19TH APRL 2021
# MY FIRST PERSONAL PROJECT
# AUTOMATE FORM FILLING FOR SPARTAN HEALTH FORM

import content as content
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://covidresponse.msu.edu/health-screening?success=Your+Spartan+Health+Screening+Form+has+been+submitted+successfully.")

driver.implicitly_wait(5)  # we wont pass this line untill 5 secs

#col = driver.find_element_by_class_name("col-md-8")

jam = driver.find_element_by_link_text("Complete Health Screening")
jam.click()
driver.implicitly_wait(5)


username = driver.find_element_by_id("msu-id")
username.send_keys("dardaniy")  # please change dardaniy to your MSU NetId USERNAME!
username.send_keys(Keys.RETURN)  # return means enter

password = driver.find_element_by_id("password")
password.send_keys("password")   # please change it to your password and run to see, this is just a sample password
password.send_keys(Keys.RETURN)

breathing = driver.find_element_by_id("breathing2")
breathing.click()
next = driver.find_element_by_id("next")
next.click()
fever = driver.find_element_by_id("fever2")
fever.click()
next.click()
cough = driver.find_element_by_id("cough2")
cough.click()
next.click()
taste = driver.find_element_by_id("lossOfSmellOrTaste2")
taste.click()
next.click()
chill = driver.find_element_by_id("chills2")
chill.click()
next.click()
muscle = driver.find_element_by_id("muscleAches2")
muscle.click()
next.click()
head = driver.find_element_by_id("headaches2")
head.click()
next.click()
throat = driver.find_element_by_id("soreThroat2")
throat.click()
next.click()
runny = driver.find_element_by_id("runnyNose2")
runny.click()
next.click()
nv = driver.find_element_by_id("nvd2")
nv.click()
next.click()
contact = driver.find_element_by_id("covidContact2")
contact.click()
driver.maximize_window()
#time.sleep(5)
next_covid = driver.find_element_by_id("next")
next_covid.click()
email = driver.find_element_by_id("other-email-1")
email.send_keys("summer93@msu.edu, rosalesn@msu.edu")
email.send_keys(Keys.RETURN)  # return means enter
submit = driver.find_element_by_id("submit")
submit.click()



#link = driver.find_element_by_link_text("")


#id="msu-id"


# try:
#      main = WebDriverWait(driver, 10).until(
#      EC.presence_of_element_located((By.ID, "content")))
#
# except:
#      driver.quit()
#







#
# cookie = driver.find_element_by_id("bigCookie")
# cookie_count = driver.find_element_by_id("cookies")
# items = [driver.find_elements_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]


# actions = ActionChains(driver)
# # what are action chains
# actions.click(cookie)
#
# for i in range(5000):
#     actions.perform()
#     count = int(cookie_count.text.split(" ")[0])
#     print(count)
#     for item in items:
#         value = int(item.text)
#         if value <= count:
#             upgrade_Actions = ActionChains(driver)
#             upgrade_Actions













# link = driver.find_element_by_link_text("Python Programming")
# link.click()
#
# try:
#     element = WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials")))
#     element.click()
#
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "sow-button-19310003")))
#     element.click()
#
#     driver.back()
#     driver.back()
#     driver.back()
#     driver.forward()
#     driver.forward()
#
# except:
#     driver.quit()







# print(driver.title)
#
# search = driver.find_element_by_name("s")  # return an object that works for the search bar
# search.send_keys("test")
# search.send_keys(Keys.RETURN)  # return means enter
#
# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )
#     articles = main.find_elements_by_tag_name("article")
#     for article in articles:
#         header = article.find_element_by_class_name("entry-summary")
#         print(header.text)
# finally:
#     driver.quit()



#driver.quit()  #quit to exit the browser

