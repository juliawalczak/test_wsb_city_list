#-*- coding: utf-8 -*-

import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Wsb(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    def search_link(self):
        driver = self.driver
        driver.get("https://www.wsb.pl/")
        select_city = Select(driver.find_element_by_id("edit-city"))
        # Sprawdzenie czy do wyboru jest 11 opcji
        self.assertEqual(11, len(select_city.ptions))
        # Sprawdzenie czy do wyboru są konkretne miasta
        act_options = []
        exp_options = [[u'Wybierz miasto', u'Bydgoszcz', u'Chorzów/Katowice', u'Gdańsk', u'Gdynia', u'Opole', u'Poznań', u'Szczecin', u'Toruń', u'Warszawa', u'Wrocław']
        for option in select_city.options:
            act_options.append(option.get_attribute("text"))
        self.assertEqual(exp_options, act_options)
            
        
        
