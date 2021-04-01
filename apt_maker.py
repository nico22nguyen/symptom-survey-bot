from selenium.webdriver.common.keys import Keys
import math
import ss_bot

DELTA = 5
apt_home_url = "https://patientconnect.bu.edu/appointments_home.aspx"

#does the math to work with times (not in base 10)
def add_time(raw, delta):
    hour = int(raw[:(len(raw) - 3)])
    minute = int(raw[len(raw) - 2:]) + delta
    hour += math.floor(minute / 60)
    hour = hour % 12
    if hour == 0:
        hour = 12
    minute = minute % 60
    minute = str(minute)
    if int(minute) < 10:
        minute = "0" + str(minute)
    return str(hour) + ":" + str(minute)

#finds and returns closest open slot to given time
def find_open_time(slot, delta, all_times):
    for row in all_times:
        if slot in row.text:
            row.find_element_by_tag_name('input').click()
            return slot

    if(delta >= 0):
        delta += DELTA
    else:
        delta -= DELTA

    delta *= -1
    output = find_open_time(add_time(slot, delta), delta, all_times)
    return output

#makes an appointment given various appointment info
def make_apt(web, DATE, apt_time, apt_loc):
    #parse day from date
    day = DATE[DATE.index("/") + 1 : DATE.index("/", DATE.index("/") + 1)]

    #navigate to actual scheduling page (past the bullshit)
    web.get(apt_home_url)
    schedule_button = web.find_element_by_xpath('//*[@id="cmdSchedule"]')
    schedule_button.click()
    ss_bot.load()

    emergency_button = web.find_element_by_xpath('//*[@id="297"]')
    emergency_button.click()
    continue_button = web.find_element_by_xpath('//*[@id="cmdProceed"]')
    continue_button.click()

    covid_button = web.find_element_by_xpath('//*[@id="496"]')
    covid_button.click()
    continue_button = web.find_element_by_xpath('//*[@id="cmdProceed"]')
    continue_button.click()
    ss_bot.load()

    agree_button = web.find_element_by_xpath('//*[@id="493"]')
    agree_button.click()
    continue_button = web.find_element_by_xpath('//*[@id="cmdProceed"]')
    continue_button.click()
    ss_bot.load()

    proceed_button = web.find_element_by_xpath('//*[@id="484"]')
    proceed_button.click()
    continue_button = web.find_element_by_xpath('//*[@id="cmdProceed"]')
    continue_button.click()
    ss_bot.load()

    no_symptoms = web.find_element_by_xpath('//*[@id="478"]')
    no_symptoms.click()
    continue_button = web.find_element_by_xpath('//*[@id="cmdProceed"]')
    continue_button.click()

    no_covid = web.find_element_by_xpath('//*[@id="498"]')
    no_covid.click()
    continue_button = web.find_element_by_xpath('//*[@id="cmdProceed"]')
    continue_button.click()

    continue_button = web.find_element_by_xpath('//*[@id="cmdStandardProceed"]')
    continue_button.click()
    ss_bot.load()
    ss_bot.load()

    location_option = web.find_element_by_xpath('//*[@id="LocationList"]')
    location_option.send_keys(apt_loc[0])
    location_option.click()

    date = web.find_element_by_xpath('//*[@id="StartDate"]')
    web.execute_script("document.getElementById('StartDate').value = '" + DATE + "';")

    search_button = web.find_element_by_xpath('//*[@id="apptSearch"]')
    search_button.click()
    ss_bot.load()

    #make appointment
    apt_made = False
    while not apt_made:
        reached_target = False
        table_rows_raw = web.find_element_by_xpath('//*[@id="apptContainer"]/fieldset/table/tbody').find_elements_by_tag_name('tr')
        table_rows = []

        #make list all pertinent rows
        for row in table_rows_raw:
            if day + "," in row.text:
                if reached_target:
                    day_name = row.text.split(",", 1)[0]
                table_rows.append(row)
                reached_target = True
            elif reached_target:
                break

        #find closest available appointment time
        apt_time = find_open_time(apt_time, 0, table_rows)

        #continue
        continue_button = web.find_element_by_xpath('//*[@id="cmdStandardProceedUpper"]')
        continue_button.send_keys(Keys.NULL)
        continue_button.click()

        #buggy BU website error handling
        try:
            submit_button = web.find_element_by_xpath('//*[@id="cmdConfirm"]')
            submit_button.click()
            print("Appointment booked for " + day_name + " " + day + " at " + apt_time)
            apt_made = True
        except:
            print("Too Slow :(, trying again...")
            continue_button = web.find_element_by_xpath('//*[@id="cmdStandardCancel"]')
            continue_button.click()
            ss_bot.load()

if __name__ == '__main__':
    #ask for day, time
    month = input('month: ').strip()
    day = input('day: ').strip()
    apt_time = input('time: ').strip()
    
    #calc date
    DATE = month + "/" + day + "/" + "2021"

    #login
    web = ss_bot.login("login_credentials.txt")

    #make appointment
    make_apt(web, DATE, apt_time, 'agganis')