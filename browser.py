#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from html.parser import HTMLParser
from abc import abstractmethod, ABCMeta
import os
import platform


class Browser(metaclass=ABCMeta):
    driver = None

    def __init__(self):
        if os.name == 'nt':
            DRIVER_PATH = 'drivers/chromedriver_win32.exe'
        elif platform.system() == 'Darwin':
            DRIVER_PATH = 'drivers/chromedriver_mac64'
        else:
            DRIVER_PATH = 'drivers/chromedriver_linux64'

        options = Options()
        # options.binary_location = setting.CHROME_BINARY_LOCATION
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=DRIVER_PATH)
        # self.driver.set_window_size(setting.SCREEN_WIDTH, 800)  # set the window size that you need
        # self.parser = HTMLParser()

    @abstractmethod
    def crawl(self):
        pass

    @abstractmethod
    def process(self):
        pass

    def __del__(self):
        self.driver.close()