# City of Tampa, Hillsborough County 

address = "3007 16th"    #Enter address here

'''
Contact Info: 
-Taxes: Mail and make payable to Tax Collector, PO Box 30012, Tampa, Florida 33630-3012. 813-635-5200 
Address: 4100 W Dr Martin Luther King Jr Blvd, Tampa, FL 33614.
-Utilities: Mail and make payable to City of Tampa Utilities, P.O. Box 30191, Tampa, FL 33630-3191. 813-274-8811 
-Permits: Mail and make payable to City of Tampa Permitting, P.O. Box 2200, Tampa, Florida 33602. 813-274-3100
-Code: Mail and make payable to Clerk of Circuit Court, P.O. Box 3360, Tampa, FL 33601. 813-274-5545 


To Do:
-Need to recode the drop down for permits as the parcel num isn't working anymore. 

'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains as AC 
# from requests_html import HTMLSessions
# from helium import *
import time

# assign .exe to var driver so it can grab pages.
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(30000)

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# options.AddExcludedArgument("enable-automation") 


# APPRAISALS:
driver.get("https://gis.hcpafl.org/PropertySearch") #opens chrome @ address (uses the driver to get the page*)
# print(driver.title)


# Finds the page element/search 
search = driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div/div/div/div/div[2]/div[1]/label[3]/input") #finding id, name or other html data
#--------------------------------------------------------------------------------------------------------------------------------

# search.send_keys("parcel_num")
search.send_keys(address) 

#--------------------------------------------------------------------------------------------------------------------------------
search.send_keys(Keys.RETURN)
# Address is now loaded.

# Must use new var for additional selectors*
ap_result = driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div/div/div/div/div[2]/div[4]/div[2]/div[4]/table/tbody/tr[1]/td[2]")
ap_result.click()
# Appraisal located!!! 

# Grabbing parcel number
page_parcel_num = driver.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/table/tbody/tr[2]/td[2]') # Parcel num on webpage
parcel_num = page_parcel_num.text  # parcel num with dash
# print(parcel_num)

dot_parcel_num = parcel_num.replace('-', '.')  # Permit search requires '.' where '-' should be
# print(dot_parcel_num) 



# printer friendly version of appraisals
a_print_friendly = driver.find_element_by_css_selector("div.export-section:nth-child(3) > a:nth-child(1) > span:nth-child(2)")

# TAXES:
# set tax selector 
taxes = driver.find_element_by_css_selector("div.export-section:nth-child(3) > a:nth-child(4) > span:nth-child(2)")
a_print_friendly.click(), taxes.click()

# PERMITS:
# uses tab to reload for searching permits
driver.get("https://aca.tampagov.net/CitizenAccess/Cap/CapHome.aspx?module=Building&TabName=Building")  # permit page
parcel_search = driver.find_element_by_css_selector("#ctl00_PlaceHolderMain_generalSearchForm_txtGSParcelNo")


parcel_search.send_keys(dot_parcel_num) # sends parcel num w/ dot
parcel_search.send_keys(Keys.RETURN)


#CODES:
# print("CURRENT WINDOW HANDLE = ", driver.current_window_handle)
# driver.execute_script(script, args) # allows for the execution of JS 
driver.execute_script('''window.open("https://webapps.hillsboroughcounty.org/hcce/resources/onlineservices/enforcement/home.cfm", "_Code_tab");''') # "_blank = name of new tab"
# the code search location above uses dynamically generated code. 
# Maybe try to print out the html contents and parse through to get address or parcel tab?
# Use Relative XPath using contains or starts with text?

# parcel_tab = driver.find_element_by_xpath("/html/body/div/main/div/form/ul/li[3]/a")
# parcel_tab = driver.execute_script('''document.getElementByInnerText("Folio / Parcel Number")''') 
# parcel_tab = driver.find_element(By.CLASS_NAME("nav-link active"))
# parcel_tab = driver.find_element_by_xpath('//a[contains(@href,"#folioTab")]')
# https://app.hillsboroughcounty.org/CodeEnforcement/Inquiry/Search/Index#folioTab
# <a class="nav-link active" data-toggle="tab" href="#folioTab">Folio / Parcel Number</a>     # element copy
# parcel_tab = driver.find_element_by_partial_link_text('[https://app.hillsboroughcounty.org/CodeEnforcement/Inquiry/Search/Index#folioTab]')
# parcel_tab = driver.find_element_by_xpath('//*[@href="#folioTab"]')
# document.querySelector("#searchForm > ul > li:nth-child(3) > a") # js path
# //*[@id="searchForm"]/ul/li[3]/a

# parcel_tab = driver.find_element_by_xpath('//*[@id="searchForm"]/ul/li[3]/a')
# parcel_tab.click() # clicks on tab
# parcel_search2 = driver.find_element_by_id("FolioNumber")
# parcel_search2.send_keys(dot_parcel_num) # enters parcel num    //*[@id="FolioNumber"]
# parcel_search2.send_keys(Keys.RETURN)


#   Code below doesn't work. 
# code_subtab = driver.find_element_by_class_name("border border-top-0 shadow p-3")
# time.sleep(1)
# code_subtab.click() 
# time.sleep(3)
# addr_search = driver.find_element_by_id("StreetAddress")
# time.sleep(2)
# addr_search.send_keys("6906 Mexicala")
# time.sleep(2)
# addr_search.send_keys(Keys.RETURN)


time.sleep(30000)
try:
    main = WebDriverWait(driver, 30 ).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    
    print(main)
except:
    main = driver.find_element_by_id("main")



