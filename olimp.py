from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.remote.webdriver import WebDriver

driver = webdriver.Firefox()
driver.get("https://olymptrade.com/")

element = driver.find_elements_by_css_selector('body > div.page__wrapper.js-central-page > div > div.flexbox-page.flexbox-page_mod-border.flexbox-page_mod-border-blue > main > div > div.flexbox-page__centred-content > figure > ul > li:nth-child(5) > a')
# print(element)








# import ast
# import time
# import argparse
#
# from selenium import webdriver
#
#
# EXECUTORS = {
#     'desktop': 'http://10.0.10.4:4444/wd/hub',
# }
# c = {'browserName': 'chrome'}
#
#
# driver = webdriver.Remote(command_executor=EXECUTORS["desktop"], desired_capabilities=c)
# driver.get("https://kvartirka.com/")
# time.sleep(5)
# driver.quit()