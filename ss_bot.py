from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
from webdriver_manager.chrome import ChromeDriverManager

def load():
    time.sleep(.5)

#logs in using USER and PASS, returns logged in web driver
def login(USER, PASS):
    #boot chrome
    web = webdriver.Chrome(ChromeDriverManager().install())

    web.get('http://patientconnect.bu.edu/')
    load()

    u_name = web.find_element_by_xpath('//*[@id="j_username"]')
    p_word = web.find_element_by_xpath('//*[@id="j_password"]')
    continue_button = web.find_element_by_xpath('//*[@id="wrapper"]/div/form/button')

    u_name.send_keys(USER)
    p_word.send_keys(PASS)
    continue_button.click()
    load()
    return web
    
#takes in logged in webdriver and does daily symptom survey
def do_survey(web):
    #access and navigate to survey
    web.get('https://patientconnect.bu.edu/Mvc/Patients/QuarantineSurvey')
    load()

    continue_button = web.find_element_by_xpath('//*[@id="mainbody"]/div[2]/div[1]/div/div[2]/a')
    continue_button.click()
    load()

    #click all NO buttons
    submit_button = web.find_element_by_xpath('//*[@id="mainbody"]/footer/div/div[2]/input')
    no_buttons = web.find_elements_by_class_name('required')
    for i in range(8):
        no_buttons[2 * i].click()

    #submit
    submit_button.click()
    print('survey complete')

if __name__ == '__main__':
    web = login("nicn", "3869544zZnN!")
    do_survey(web)
    web.quit()