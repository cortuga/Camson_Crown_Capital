#Muni template for automation

# __ County

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  >ENTER ADDRESS BELOW<

full_address = "111 main"

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains as AC 
# from requests_html import HTMLSessions
# from helium import *
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver.implicitly_wait(30000)

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# options.AddExcludedArgument("enable-automation")

# APPRAISALS:  ----------------------------------------------------------------
driver.get("https://www.ocpafl.org/searches/ParcelSearch.aspx") #opens chrome @ address (uses the driver to get the page*)
# print(driver.title)
# time.sleep(2) # tells the bot to wait to load the page.
agree = driver.find_element_by_id("popup_ok")
agree.click()
# time.sleep(1)
exitX = driver.find_element_by_id("ctl00_ctl00_ctl00_ctl00_ContentMain_ctl03_PopupPanel1_CloseButton")
exitX.click()
time.sleep(2)

'''
# Grabbing parcel number  -----------------------
page_parcel_num = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_PanelResults"]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/div/a') 
parcel_num = page_parcel_num.text  # parcel num with dash
print(parcel_num)
# for i in parcel_num:
#     if i == " ":
#         break
#     print(parcel_num)
    '''

    # time.sleep(300)
# dot_parcel_num = parcel_num.replace('-', '.')  # Permit search requires '.' where '-' should be
# print(dot_parcel_num) -------------------------------

# TAXES:
# set tax selector 
driver.execute_script('''window.open("https://www.octaxcol.com/taxes/about-property-tax/property-tax-search-tax-roll-download/
", "_Taxes_tab");''') # "_blank = name of new tab"
time.sleep(5)

# UTILITIES: 
'''The plan for this section is to automate the sending of the email using the basic form for the ocu format. May need to compile a list or hardcode the email of the correct address.
-will need to log into Camson gmail
-be able to compose new email
-copy and paste in txt from this document + (Address, Parcel #, Owner name) 
'''

# PERMITS:   ----------------------------------------------------
driver.execute_script('''window.open(" ", "_Permits_tab");''') # "_blank = name of new tab"
# time.sleep(5)
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ctl00_PlaceHolderMain_generalSearchForm_txtGSNumber_ChildControl0']"))).send_keys(address_num)
# street_no = driver.find_element_by_xpath("//*[@id='ctl00_PlaceHolderMain_generalSearchForm_txtGSNumber_ChildControl0']")
# street_no.send_keys(address_num)
# street_nam = driver.find_element_by_xpath("//*[@id='ctl00_PlaceHolderMain_generalSearchForm_txtGSStreetName']")
# street_nam.send_keys(address_st)
# time.sleep(1)
# street_nam.send_keys(Keys.RETURN)

#CODES:  ------------------------------------------------------------------
# print("CURRENT WINDOW HANDLE = ", driver.current_window_handle)
# driver.execute_script(script, args) # allows for the execution of JS 
driver.execute_script('''window.open(" ", "_Code_tab");''') # "_blank = name of new tab"
log_UN = driver.find_element_by_xpath("//*[@id='ctl00_PlaceHolderMain_LoginBox_txtUserId']")
log_UN.send_key("camson.crown.capital@gmail.com")
log_PW = driver.find_element_by_xpath("//*[@id='ctl00_PlaceHolderMain_LoginBox_txtPassword']")
log_PW.send_keys("Pa^^word1234")
time.sleep(3)

time.sleep(30000)
try:
    main = WebDriverWait(driver, 30 ).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    
    print(main)
except:
    main = driver.find_element_by_id("main")