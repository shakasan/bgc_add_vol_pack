#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Copyright (C) 2016   Tuxicoman

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

---

Script modified by : 
  Francois B. (Makotosan/Shakasan)

Github : 
  https://github.com/shakasan/bgc_add_vol_pack

Changelog :
    - Updated for Python3
    - Any volume pack sizes
    - WebDriverWait increased up to 20 to try to avoid login failures
    - Headless mode added as optional parameter
    - repeat and packSize are optional with default value to 1 pack of 150 GB
"""

import argparse
parser = argparse.ArgumentParser(description='Add extra data volume pack to Belgacom Internet')
parser.add_argument('login', type=str, help='Belgacom login email')
parser.add_argument('password', type=str, help='Belgacom password')
parser.add_argument('--repeat', type=int, default=1, help='Number of volume packs to add (1 pack by default)')
parser.add_argument('--packSize', type=str, default='150', help='Volume size of the pack to add (150 GB by default)')
parser.add_argument('--headless', type=int, default=1, help='Headless mode (enabled by default ; using xvfb)') #, action='store_true'
args = parser.parse_args()

try:
  import selenium
except ImportError:
  print ("Cannot import selenium. Try: $ pip3 install --user selenium")
  sys.exit()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

if args.headless :
  try:
    import pyvirtualdisplay
  except ImportError:
    print ("Cannot import pyvirtualdisplay. Try: $ pip3 install --user pyvirtualdisplay")
    sys.exit()

  from pyvirtualdisplay import Display
  display = Display(visible=0, size=(1920, 1080))
  display.start()

browser = webdriver.Firefox()

print ("Login ...")
browser.get('https://www.belgacom.be/login/fr/?ru=https%3A%2F%2Fadmit.belgacom.be%2F&pv=fls')
browser.switch_to_frame(browser.find_element_by_xpath('//iframe[@name="loginIframe"]'))
browser.switch_to_frame(browser.find_element_by_xpath('//iframe[@name="frame"]'))
browser.find_element_by_xpath('//input[@id="loginForm:userName"]').send_keys(args.login)
browser.find_element_by_xpath('//input[@id="loginForm:password"]').send_keys(args.password)
browser.find_element_by_xpath('//input[@id="loginForm:continue"]').click()
wait = WebDriverWait(browser, 20)
wait.until(lambda browser: browser.find_element_by_xpath('//div[@data-tms-id="TMS_myBillAndProducts"]'))
print ("Login done")

browser.find_element_by_xpath('//i[contains(@class, "icon-Internetlaptop")]').click()

for i in range(args.repeat):
  print ("Round :", i+1)
  print ("Choosing Volume pack " + args.packSize + " free")
  wait.until(lambda browser: browser.find_element_by_xpath('//a[@href="#pb-tabs-notActivated"]'))
  browser.find_element_by_xpath('//a[@href="#pb-tabs-notActivated"]').click()

  elements = browser.find_elements_by_xpath('//span[contains(@class,"og-unit")]')
  for element in elements :
    extraVol = "Extra Volume " + args.packSize + " GB"
    if extraVol in element.get_attribute("innerHTML"):
      element.click()
      break

  myProduct = "myProducts/myOrder?selectedOption=hbs_volume_pack_" + args.packSize + "_free"
  browser.find_element_by_xpath('//a[contains(@href,"' + myProduct + '")]').click()

  wait.until(lambda browser: browser.find_element_by_xpath('//a[contains(@class,"pcp-order-next")]'))
  browser.find_element_by_xpath('//a[contains(@class,"pcp-order-next")]').click()

  print ("Approving general terms")
  wait.until(lambda browser: browser.find_element_by_xpath('//input[@id="generalTerms"]'))
  browser.find_element_by_xpath('//input[@id="generalTerms"]').click()
  browser.find_element_by_xpath('//a[@eventdetail="confirmOrderLink"]').click()

  print ("Confirmation")
  browser.find_element_by_xpath('//a[@href="/eservices/wps/myportal/myProducts"]').click()

browser.quit()

if args.headless == "yes":
  display.stop()
