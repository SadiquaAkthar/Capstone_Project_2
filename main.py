from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from Data import data
from Locators import locators
import time
import pytest

class Project:
    # constructor
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.action = ActionChains(self.driver)
        self.driver.get(data.WebApp_Data().url)
    
    # Test Case 1: Forgot Password link validation
    def test_forgot_password(self):

        # Precondition
        #  Launch URL and Click on "Forgot Password" link.
        wait=WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, locators.WebApp_Locators.forgot_pass))).click()
        
        # Steps
        try:
            # Check if Username textbox is visible and Provide your username
            wait.until(EC.visibility_of_element_located((By.NAME, locators.WebApp_Locators.username_input_box))).send_keys(data.WebApp_Data.username)
            wait.until(EC.visibility_of_element_located((By.XPATH,locators.WebApp_Locators.reset_pass_btn))).click()
            
            #Expected result: successful message saying "Reset Password link sent successfully".
            success_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.WebApp_Locators.reset_succ_msg)))
            assert "Reset Password link sent successfully" in success_message.text
            print("PASS  : Reset Password Successful")
        
        except ElementNotVisibleException as selenium_error:
            print(selenium_error)
            print("FAIL  : Reset Password Unsuccessful")
                     
    # Test Case 2: Header Validation on Admin Page
    def test_admin_page_header(self):

        try:
        
            # Launch URL and Login as "Admin"
            self.login(data.WebApp_Data().username,data.WebApp_Data().password)
            wait = WebDriverWait(self.driver, 10)
            
            # Steps
            # Go to Admin page and Validate "Title" of the page as "OrangeHRM
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT,'Admin'))).click()
            assert "OrangeHRM" in self.driver.title
            print("PASS  : Validation of Title Successful")
            
            # Expected Result    
            page_header=wait.until(EC.visibility_of_element_located((By.XPATH,locators.WebApp_Locators.page_head_Admin)))
            self.items =page_header.find_element(By.TAG_NAME,"li")
            
            # Validate options on Admin page
            for self.items in data.WebApp_Data.admin_options:
                print("PASS  : Validation of ",self.items," on Admin page Successful")

            #logout successfully
            self.logout()
        
        except ElementNotVisibleException as selenium_error:
            print(selenium_error)
            print("FAIL  : ",self.items,"  Unsuccessful")

        finally:
            self.driver.refresh()
            
                
        
    # Test Case 3: Main Menu Validation on Admin Page
    def test_admin_page_menu(self):

        try:
            # Launch URL and Login as "Admin"
            self.login(data.WebApp_Data().username,data.WebApp_Data().password)
            wait = WebDriverWait(self.driver, 10)

            # Validate Menu options           
            page_menu=wait.until(EC.visibility_of_element_located((By.XPATH, locators.WebApp_Locators.menu_items_header)))
            self.mitems=page_menu.find_element(By.TAG_NAME,"li")
            
            # Expected Result
            # Admin Page Menu Items on Admin Page are visible
            for self.mitems in data.WebApp_Data.menu_items:
                assert self.mitems in self.driver.page_source
                print("PASS  : Validation of ",self.mitems," Successful")

            
            #logout successfully
            self.logout()
        

        except ElementNotVisibleException as selenium_error:
            print(selenium_error)
            print("FAIL  : ",self.mitems,"  Unsuccessful")

        finally:
            self.driver.quit()


    def login(self,uname,passw):
            
            try:
                self.driver.maximize_window()
                self.driver.get(data.WebApp_Data().url)
                self.driver.implicitly_wait(20)
                self.driver.find_element(by=By.NAME, value=locators.WebApp_Locators().username_input_box).send_keys(uname)
                self.driver.find_element(by=By.NAME, value=locators.WebApp_Locators().password_input_box).send_keys(passw)
                self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().submit_button).click()
            
            except NoSuchElementException as selenium_error:
                print(selenium_error)

    def logout(self):
         
         logout_button = self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators.logout_button)
         action = ActionChains(self.driver)
         action.click(on_element=logout_button).perform()
         self.driver.find_element(by=By.LINK_TEXT, value='Logout').click()
         

def test_main():
    obj1=Project()
    obj1.test_forgot_password()
    obj1.test_admin_page_header()
    obj1.test_admin_page_menu()

