# -*- coding:utf-8 -*-
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

# browser.get("http://www.csdn.net")

print browser.find_element_by_xpath('//body')
print browser.page_source
browser.close()

'''
http://selenium-python.readthedocs.io/
'''

"""
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector


ind_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector

"""