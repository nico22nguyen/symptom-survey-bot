# ss_bot
  - Logs into patient connect
  - Completes daily BU symptom survey screening
  - Serves as helper module for daily_pc_bot
  
# apt_maker
  - Logs into patient connect
  - Books closest open appointment for given day, time
  - Provides appointment scheduling functionality for daily_pc_bot
 
# daily_pc_bot
  - 1 stop shop for all things patient connect (to be run daily)
  - Logs into patient connect
  - Completes symptom survey
  - Determines if/when an appointment needs to be scheduled
  - If the bot finds that you have no appointment, it schedules one on the proper day
  - Default appointment time = "1:00", default appointment location = "agganis"
          to change these, simply change the values passed into apt_maker()
          
  NOTE: When running these modules locally, be sure to create file (default = login_credentials.txt) with your BU Username on the first line and your BU Password on the second line

--> Dependencies <--
selenium
webdriver_manager.chrome
