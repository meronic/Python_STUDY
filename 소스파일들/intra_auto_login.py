from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()

url = 'https://intra.wku.ac.kr'

driver.get(url)  #대학교 웹정보 서비스 홈페이지 접속

action = ActionChains(driver)


driver.find_element_by_css_selector('#userid').send_keys('hen3633')
driver.find_element_by_css_selector('#passwd').send_keys('you1288')
driver.find_element_by_css_selector('#passwd').send_keys(Keys.ENTER)
##action.send_keys('akrasia3633').perform() # id 입력
##driver.find_element_by_css_selector('.CwaK9').click() # 클릭
##
##time.sleep(2) #기다리기 위한 시간 2초 
##
##driver.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys('you1288@') # 비밀번호 입력
##driver.find_element_by_css_selector('.CwaK9').click() # 클릭



















