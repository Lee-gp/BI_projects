from lxml import etree
import time
from selenium import webdriver
import pandas as pd

#使用ChromeDriver
dirver = webdriver.Chrome()
#设置想要下载的导演和链接
director = u"徐峥"
base_url = "http://movie.douban.com/"