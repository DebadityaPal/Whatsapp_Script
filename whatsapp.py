from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 
import time

driver = webdriver.Chrome(executable_path=r'C:\...\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

all_names = ['Parth IIITM','asdasd','H3LL0FR13ND']
imgpath =  r'C:\...\image'
file1path= r'C:\...\file1'
file2path= r'C:\...\file2'
msg = "Message"
input('Enter anything after scanning QR code')

search_box = driver.find_element_by_class_name('eiCXe')
for name in all_names:
    print(name)

    search_box.send_keys(name)
    time.sleep(1)
   
    if not len(driver.find_elements_by_xpath('//span[@title = "{}"]'.format(name))) > 0: 
        search_box.send_keys(Keys.CONTROL + "a")
        search_box.send_keys(Keys.DELETE)
        continue

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_3u328')
    msg_box.send_keys(msg)
    send = driver.find_element_by_class_name('_3M-N-')
    send.click()
    
    attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()
    file_box = driver.find_element_by_xpath('//input[@accept="*"]')
    file_box.send_keys(file1path)
    send_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send-light"]')))
    send_button.click()
    time.sleep(1)

   
    attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()
    file_box = driver.find_element_by_xpath('//input[@accept="*"]')
    file_box.send_keys(file2path)
    send_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send-light"]')))
    send_button.click()
    time.sleep(1)

   
    attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()
    file_box = driver.find_element_by_xpath('//input[@accept="*"]')
    file_box.send_keys(imgpath)
    send_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send-light"]')))
    send_button.click()
    time.sleep(1)
