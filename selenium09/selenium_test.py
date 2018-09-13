
# 练习1
# #coding = utf-8
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
#
# driver.find_element_by_id("kw").send_keys("Selenium2")
# driver.find_element_by_id("su").click()
# time.sleep(5)
# # driver.quit()
# driver.find_element_by_id("kw").clear()

#练习2 checkbox
#coding = utf-8
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get("http://www.douban.com")
#
# driver.find_element_by_name("remember").click()
# time.sleep(5)
# driver.find_element_by_name("remember").click()

#练习3  select
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import time
# driver = webdriver.Chrome()
# driver.get("http://www.dobai.cn")
#
# Select(driver.find_element_by_name("jumpMenu")).select_by_index(1)


#练习4
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import time
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
#
# for cookie in driver.get_cookies():
#     print(cookie)

#练习5
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.douban.com/")
# driver.implicitly_wait(20)
element = WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.ID,'form_email'))
)
print(element)
# driver.find_element_by_id("hdfgdj")

