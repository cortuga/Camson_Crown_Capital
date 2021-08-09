# City of Tampa, Hillsborough County 

from tkinter import *
from tkinter import simpledialog   #input input()
from tkinter import messagebox   #output print()
# from PIL import ImageTk, Image
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains as AC 
# from requests_html import HTMLSessions
# from helium import *
import time
# import pyautogui
# assign .exe to var driver so it can grab pages.

#:::::::::::::::::::::::::::::::::::::::::::::::::::Splash Screen
# splash_root = Tk()
# splash_root.title("Camson Crown Capital")
# splash_root.geometry("330x200+-1500+200")

# splash_label = Label(splash_root, text="splash screenxxx")
# splash_label.pack()

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::GUI
# def get_address():   #showinfo, showwarning, showerror, askquestion, askokcancel,  "ok" or "cancel" return 1 or 0

#     address_Input = simpledialog.askstring(title= "Property Address", prompt= "Please enter address:")
#     print("User input was - ", address_Input) 
#     # return address_Input
#     close_win()
    
    
# Get user input for parcel number:
#parcel_Input = simpledialog.askinteger(title="Parcel Number", prompt="Parcel Number")
#============================================================================================
# def close_win():
#     window.destroy()

# entered_text = "x"
# def click():
#     global entered_text
#     entered_text = textentry.get()
#     # global entered_text
#     # print(entered_text)
#     close_win()
#     return entered_text
    


# window = Tk()
# window.title('Camson Crown (Uni. Hillsborough)')
# window.configure(background="light grey")
# window.geometry("400x300")

# #   Open image
# org_pic = Image.open("Hillsborough.Unincorporated/CCC Logo2a.png")
# #   Resize image
# resized = org_pic.resize((400, 300), Image.ANTIALIAS)

# new_pic = ImageTk.PhotoImage(resized)

# my_label= Label(window, image=new_pic)
# my_label.pack()

# #   create text entry box:
# textentry = Entry(window, width=30, bg="white", borderwidth=5)   #textVariable=enteredAddress, Default val = .!entry
# textentry.place(x=170, y=1)
# # entered_text = textentry     #default val is .!entry
# placeholder = "Example: 1015 Mexicala"
# textentry.insert(0, placeholder)
# print()

# #create text box label:
# entry_box_label = Label(window, text="Address here -->")
# entry_box_label.place(x=65, y=4)

# #   add a submit button:
# submit_button = Button(window, text="SUBMIT", width=9, command=click)
# submit_button.place(x=170, y=35)

# window.mainloop() # root.mainloop will need to be at the end of the gui setup 

#=========================================================================
class EntryWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title('Camson Crown (Uni. Hillsborough)')
        self.window.configure(background="white")
        self.window.geometry("400x300")

        # # Open image:
        # self.org_pic = Image.open("Hillsborough.Unicorporated\CCC Logo2a.png")
        # # Resize image:
        # self.resized = org_pic.resize((400, 300), Image.ANTIALIAS)
        # self.new_pic = ImageTk.PhotoImage(resized)
        # # Labels for img:
        # self.my_label = Label(EntryWindow, image=new_pic)
        # # self.my_label.pack()


        #   create text entry box:
        self.textentry = Entry(self.window, width=20, bg="white", borderwidth=5, font=(20))   #textVariable=enteredAddress, Default val = .!entry
        self.textentry.place(x=160, y=120)
        self.placeholder = "Example: 1015 Mexicala"
        self.textentry.insert(0, self.placeholder)
        self.property_address = ''

        #create text box label:
        self.entry_box_label = Label(self.window, text="Address here ->", font=(20))
        self.entry_box_label.place(x=37, y=123)

        #   add a submit button:
        self.submit_button = Button(self.window, text="SUBMIT", width=19, font=(35), command=self.submit)
        self.submit_button.place(x=165, y=150)

        self.window.mainloop()

    def submit(self):
        self.property_address = self.textentry.get()
        self.window.destroy()
        return '{}'.format(self.property_address)  # not sure if this return is needed. 


main_window = EntryWindow()
print(main_window.property_address)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::     Selenium Start

propertyAddress = main_window.property_address # default "1015 Mexicala"  



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

from selenium.webdriver.chrome.options import Options
chrome_options = Options()

# PATH = "C:\Program Files (x86)\chromedriver.exe"
# op = webdriver.ChromeOptions()
# op.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
# op.add_argument("--headless")
# op.add_argument("--no-sandbox")
# op.add_argument("--disable-dev-sh-usage")

# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
# PATH = "/usr/bin/google-chrome"
# driver = webdriver.Chrome(PATH)
# >>>>>>> 2e49cc0572eec9ddd2d04fae3a0f8f5d45629ad6
# Options().binary_location = os.environ.get("GOOGLE_CHROME_BIN")

#To explain whats heppening below: (https://medium.com/@romik.kelesh/how-to-deploy-a-python-web-scraper-with-selenium-on-heroku-1459cb3ac76c)
# Options().add_argument("--headless") # will open without chrome window
# Options().add_argument("--disable-dev-shm-usage")#Implement traditional shared memory. NOTE: will write shared memory files into /tmp instead of /dev/shm
# Options().add_argument("--no-sandbox")      #is an additional feature from Chrome, which aren’t included on the Linux box that Heroku spins up for you
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"))#, chrome_options=chrome_options)
driver.implicitly_wait(10000)
# chrome_options.add_experimental_option("detach", True)
# options.AddExcludedArgument("enable-automation") 



# APPRAISALS:
driver.get("https://gis.hcpafl.org/PropertySearch") #opens chrome @ address (uses the driver to get the page*)
# print(driver.title)


# Finds the page element/search 
search = driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div/div/div/div/div[2]/div[1]/label[3]/input") #finding id, name or other html data
#--------------------------------------------------------------------------------------------------------------------------------

# search.send_keys("parcel_num")
search.send_keys(propertyAddress) 

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



