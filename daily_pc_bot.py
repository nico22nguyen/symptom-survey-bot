import sys
import ss_bot
import apt_maker

apt_home_url = "https://patientconnect.bu.edu/appointments_home.aspx"

#takes in logged in web driver, returns next required apt_date (string)
def get_apt_date(web):
    web.get('http://patientconnect.bu.edu/')
    web.find_element_by_xpath('//*[@id="showQuarantineBadge"]').click()
    loaded = False
    while not loaded:
        try:
            apt_string = web.find_element_by_id('nextlab').text
            loaded = True
        except:
            loaded = False
    base_ind = apt_string.index(": ") + 2
    return apt_string[base_ind : apt_string.index(" ", base_ind)]


if __name__ == '__main__':
    apt_made = False

    #login
    web = ss_bot.login("nicn", "3869544zZnN!")
    #do survey
    ss_bot.do_survey(web)

    #determine if i have an appointment (apointments page)
    #if so, exit program here
    web.get(apt_home_url)
    try:
        apt_container = web.find_element_by_xpath('//*[@id="appt-container"]')
        apt_made = True
    except:
        pass

    if apt_made:
        sys.exit()
        web.quit()

    #if not, determine when i need an appointment
    DATE = get_apt_date(web)

    #make the appointment
    apt_maker.make_apt(web, DATE, "1:00", "agganis")