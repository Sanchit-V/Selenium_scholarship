from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

from additional_info import add_info
from new import driver_class
from login_page import login_page
from new import driver_class
from personal_details import personal_details
from welcompage import welcomepage
from welcompage import  Logged_in_toast
from birth_details import birth_details,nation,state,city,nationality
from income_expense import income_expense,financially_independent
from children_details import has_children
from client_contact import Email, default_email, def_Phone_number, def_Whatsapp_number, additional_contact, \
    additional_whatsapp, country_code, address_nationality, Housing_type, enter_phone_number, Housing_conditions, \
    Zip_code, home_Address

language=driver_class.language



driver=driver_class.driver
pass_key=driver_class.pass_key
driver.get('http://localhost:3000')
driver.maximize_window()
time.sleep(5)

def test_Language_Button_Click():
    driver.find_element(By.CSS_SELECTOR, '[data-test-id="select-language"]').click()
    time.sleep(1)

def test_Login_page():
    login_page()
def test_Welcome_page():
    welcomepage()
def test_login_toast():
    Logged_in_toast()
def test_get_started_button():
    driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-get-started-welcome"]').click()
    time.sleep(2)
def test_Personal_Details():
    personal_details()
def test_Birth_Details():
    birth_details()
def test_Nation():
    nation()
def test_State():
    state()
def test_City():
    city()
def test_Nationality():
    nationality()
def test_Income_Expense():
    income_expense()
def test_Financially_Independent():
    financially_independent()
def test_Has_Children():
    has_children()
def test_Personal_Details_Continue_Button():
    driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-continue-personal"]').click()
    time.sleep(4)
def test_default_Email():
    default_email()

def test_add_Email():
    Email()
    time.sleep(2)

def test_Phone_number_def():
    def_Phone_number()

def test_Whatsapp_number_def():
    def_Whatsapp_number()

def test_additional_phone():
    additional_contact()

def test_additional_whatsapp():
    additional_whatsapp()

def test_country_code():
    country_code()

def test_address_Nationality():
    address_nationality()

def test_housing_type():
    Housing_type()

def test_additional_contact():
    enter_phone_number()

def test_housing_conditions():
    Housing_conditions()

def test_Zip_code():
    Zip_code()

def test_home_address():
    home_Address()

def test_continue_button_2():
    driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-continue-address"]').click()
    time.sleep(4)

def test_additional_info_page():
    add_info()

def test_finalize_button():
    driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-continue-additional"]').click()

    time.sleep(7)

def test_check_button_tnc():
    driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
    driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-send-summary"]').click()

    time.sleep(5)

def test_form_submitted():
    submitted_message=driver.find_element(By.CSS_SELECTOR, '[data-test-id="text-submitted-title"]').text

    if 'Form Submission Successful' in submitted_message:
        print('Form Submitted')

    else:
        'No submission.'

    time.sleep(2)








































    







