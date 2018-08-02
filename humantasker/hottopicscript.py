from bs4 import BeautifulSoup as soup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Import the vairables necessary ie profiles and Keywords

# LINK SCRAPPER #
def hts(# Input Vars here)
    base_url = 'https://www.hottopic.com/funko/?sz=600&start=0'
    ActiveClient = requests.get(base_url)
    raw_active_html = ActiveClient.content
    base_soup = soup(raw_active_html, "html.parser")

    # CART LINK #
    cart = 'https://www.hottopic.com/cart'

    # SETS WEBDRIVER #
    driver = webdriver.Chrome()
    
    for table_row in base_soup.findAll("div", {"class":"search-result-content four-tiles"}):
        for table_cell in table_row.findAll("div", {"class":"product-tile"}):
            for link in table_cell.findAll("a", {"class":"thumb-link"}):
                links = link.get('href')
                if keyword1 in links:
                    print(links)
                    product = links
                    # GETS THE PRODUCT LINK & BYPASSES OVERLAY #
                    driver.get(product)
                    driver.refresh()

                    add_to_cart = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart"]')));
                    add_to_cart.click();

                    # GOES TO CART URL #
                    driver.get(cart)
                    checkout_one = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout-form"]/fieldset/div/button')));
                    checkout_one.click();

                    # AUTOMATED OPERATIONS BELOW #
                    bypass_button = driver.find_element_by_name("dwfrm_login_unregistered")
                    bypass_button.click()

                    # USER FORM AUTOMATION #
                    email_form = driver.find_element_by_id("dwfrm_singleshipping_email_emailAddress")
                    email_form.send_keys(email)
                    first_name_form = driver.find_element_by_id("dwfrm_singleshipping_shippingAddress_addressFields_firstName")
                    first_name_form.send_keys(f_name)
                    last_name_form = driver.find_element_by_id("dwfrm_singleshipping_shippingAddress_addressFields_lastName")
                    last_name_form.send_keys(l_name)
                    zip_form = driver.find_element_by_id("dwfrm_singleshipping_shippingAddress_addressFields_postal")
                    zip_form.send_keys(zip)
                    ad_one_form = driver.find_element_by_id("dwfrm_singleshipping_shippingAddress_addressFields_address1")
                    ad_one_form.send_keys(ad_one)
                    ad_two_form = driver.find_element_by_id("dwfrm_singleshipping_shippingAddress_addressFields_address2")
                    ad_two_form.send_keys(ad_two)
                    city_form = driver.find_element_by_id("dwfrm_singleshipping_shippingAddress_addressFields_city")
                    phone_form = driver.find_element_by_id("dwfrm_singleshipping_shippingAddress_addressFields_phone")
                    phone_form.send_keys(phone)

                    # EXITS COOKIE WRAPPER WINDOW BUTTON OF PAGE #
                    # MAYBE NOT NECESSARY, WAS AN ATTEMPT TO FIX THE OVERLAY ISSUE WITH "CONTINUE_ONE"
                    exit_cookie = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="policy-wrapper"]/div/div/button')));
                    exit_cookie.click();

                    time.sleep(3)
                    print("YOU MUST CLICK THE RED BUTTON")

                    # ISSUE WITH THIS CONTINUE BUTTON #

                    '''
                    continue_one = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="dwfrm_singleshipping_shippingAddress"]/div[2]/fieldset/div/button/span')));
                    continue_one.click();
                    '''

                    # CARD FORM AUTO #
                    card_owner_form = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="dwfrm_billing_paymentMethods_creditCard_owner"]')));
                    card_owner_form.send_keys(card_name);

                    card_number_form = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="dwfrm_billing_paymentMethods_creditCard_number"]')));
                    card_number_form.send_keys(card_num);

                    sec_form = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="dwfrm_billing_paymentMethods_creditCard_cvn"]')));
                    sec_form.send_keys(card_cvv);

                    if month == '1':
                        mon_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_month"]/option[1]')
                        mon_act.click()
                    elif month == '2':
                        mon_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_month"]/option[2]')
                        mon_act.click()
                    elif month == '3':
                        mon_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_month"]/option[3]')
                        mon_act.click()
                    elif month == '4':
                        mon_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_month"]/option[4]')
                        mon_act.click()
                    elif month == '5':
                        mon_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_month"]/option[5]')
                        mon_act.click()
                    elif month == '6':
                        mon_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_month"]/option[6]')
                        mon_act.click()
                    elif month == '7':
                        mon_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_month"]/option[7]')
                        mon_act.click()
                    elif month == '8':
                        mon_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_month"]/option[8]')
                        mon_act.click()
                    elif month == '9':
                        mon_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_month"]/option[9]')
                        mon_act.click()
                    elif month == '10':
                        mon_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_month"]/option[10]')
                        mon_act.click()
                    elif month == '11':
                        mon_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_month"]/option[11]')
                        mon_act.click()
                    else:
                        mon_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_month"]/option[12]')
                        mon_act.click()

                    if year == '2018':
                        year_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_year"]/option[1]')
                        year_act.click()
                    elif year == '2019':
                        year_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_year"]/option[2]')
                        year_act.click()
                    elif year == '2020':
                        year_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_year"]/option[3]')
                        year_act.click()
                    elif year == '2021':
                        year_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_year"]/option[4]')
                        year_act.click()
                    elif year == '2022':
                        year_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_year"]/option[5]')
                        year_act.click()
                    elif year == '2023':
                        year_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_year"]/option[6]')
                        year_act.click()
                    elif year == '2024':
                        year_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_year"]/option[7]')
                        year_act.click()
                    elif year == '2025':
                        year_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_year"]/option[8]')
                        year_act.click()
                    elif year == '2026':
                        year_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_year"]/option[9]')
                        year_act.click()
                    else:
                        year_act = driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_year"]/option[10]')
                        year_act.click()

                    time.sleep(.25)
                    continue_two = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="dwfrm_billing"]/div[3]/button/div')));
                    continue_two.click();

                    # PLACES ORDER #
                    place_order = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="summarySubmit"]')));
                    place_order.click();

                    bool = input('Did the order go through? ')

                    if bool == 'yes':
                        webdriver.quit()
                    else:
                        place_order = WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="summarySubmit"]')));
                        place_order.click();

                else:
                    continue
