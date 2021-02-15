# Orange County

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


# Finds the page element/search box
add_search0 = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_ctl00_ctl00_ContentMain_ContentMain_ContentMain_ContentMain_TabContainer1_Searches_SubTabContainer1_QuickSearches_CompositAddressSearch1_AddressSearch1_ctl00_Address"]') #finding id, name or other html data
add_search0.send_keys(full_address) 
add_search0.send_keys(Keys.RETURN)            
time.sleep(3)


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


time.sleep(3)
# printer friendly version of appraisals
# a_print_friendly = driver.find_element_by_css_selector("div.export-section:nth-child(3) > a:nth-child(1) > span:nth-child(2)")

# TAXES:
# set tax selector 
driver.execute_script('''window.open("https://www.octaxcol.com/taxes/about-property-tax/property-tax-search-tax-roll-download/
", "_Taxes_tab");''') # "_blank = name of new tab"
time.sleep(5)

taxes = driver.find_elements_by_id("mainContent_txtSitus")
taxes.send_keys(full_address)
taxes.send_keys(Keys.RETURN)
time.sleep(2)
# # a_print_friendly.click()
# taxes.click()
# time.sleep(2)
# tax_search = driver.find_element_by_xpath('//*[@id="search_query"]')
# tax_search.send_keys(full_address)
# leaving_site.click()

time.sleep(2)

# PERMITS:   ----------------------------------------------------
driver.execute_script('''window.open("https://aca-pasco.accela.com/pasco/Cap/CapHome.aspx?module=Permits&TabName=Permits&TabList=Home%7C0%7CPermits%7C1%7CLicenses%7C2%7CEnforcement%7C3%7CCurrentTabIndex%7C1", "_Permits_tab");''') # "_blank = name of new tab"
# time.sleep(5)
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ctl00_PlaceHolderMain_generalSearchForm_txtGSNumber_ChildControl0']"))).send_keys(address_num)
# street_no = driver.find_element_by_xpath("//*[@id='ctl00_PlaceHolderMain_generalSearchForm_txtGSNumber_ChildControl0']")
# street_no.send_keys(address_num)
# street_nam = driver.find_element_by_xpath("//*[@id='ctl00_PlaceHolderMain_generalSearchForm_txtGSStreetName']")
# street_nam.send_keys(address_st)
# time.sleep(1)
# street_nam.send_keys(Keys.RETURN)


# parcel_search.send_keys(dot_parcel_num) # sends parcel num w/ dot
# time.sleep(4)
# parcel_search.send_keys(Keys.RETURN)
# time.sleep(2)


#CODES:  ------------------------------------------------------------------
# print("CURRENT WINDOW HANDLE = ", driver.current_window_handle)
# driver.execute_script(script, args) # allows for the execution of JS 
driver.execute_script('''window.open("https://webapps.hillsboroughcounty.org/hcce/resources/onlineservices/enforcement/home.cfm", "_Code_tab");''') # "_blank = name of new tab"
log_UN = driver.find_element_by_xpath("//*[@id='ctl00_PlaceHolderMain_LoginBox_txtUserId']")
log_UN.send_key("camson.crown.capital@gmail.com")
log_PW = driver.find_element_by_xpath("//*[@id='ctl00_PlaceHolderMain_LoginBox_txtPassword']")
log_PW.send_keys("Pa^^word1234")
time.sleep(30000)
# the code search location above uses dynamically generated code. 
# Maybe try to print out the html contents and parse through to get address or parcel tab?
# Use Relative XPath using contains or starts with text?

# parcel_tab = driver.find_element_by_xpath("/html/body/div/main/div/form/ul/li[3]/a")
# parcel_tab = driver.execute_script('''document.getElementByInnerText("Folio / Parcel Number")''') 
# parcel_tab = driver.find_element(By.CLASS_NAME("nav-link active"))
# parcel_tab = driver.find_element_by_xpath('//a[contains(@href,"#folioTab")]')
# https://app.hillsboroughcounty.org/CodeEnforcement/Inquiry/Search/Index#folioTab
# <a class="nav-link active" data-toggle="tab" href="#folioTab">Folio / Parcel Number</a>     # element copy
parcel_tab = driver.find_element_by_partial_link_text('[https://app.hillsboroughcounty.org/CodeEnforcement/Inquiry/Search/Index#folioTab]')
# parcel_tab = driver.find_element_by_xpath('//*[@href="#folioTab"]')
# document.querySelector("#searchForm > ul > li:nth-child(3) > a") # js path
# //*[@id="searchForm"]/ul/li[3]/a

# parcel_tab = driver.find_element_by_xpath('//*[@id="searchForm"]/ul/li[3]/a')
parcel_tab.click() # clicks on tab
time.sleep(20)
parcel_search2 = driver.find_element_by_id("FolioNumber")
# parcel_search2.send_keys(dot_parcel_num) # enters parcel num    //*[@id="FolioNumber"]
parcel_search2.send_keys(Keys.RETURN)


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