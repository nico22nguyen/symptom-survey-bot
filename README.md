# ss_bot
  - Logs into patient connect
  - Completes daily BU symptom survey screening
  - Serves as helper module for daily_pc_bot
  
# apt_maker
  - Provides appointment scheduling functionality for daily_pc_bot
 
# daily_pc_bot
  - 1 stop shop for all things patient connect (to be run daily)
  - Logs into patient connect
  - Completes symptom survey
  - Determines if/when an appointment needs to be scheduled
  - If the bot finds that you have no appointment, it schedules one on the proper day
  - Default appointment time = "1:00", default appointment location = "agganis"
          to change these, simply change the values passed into apt_maker()
          
  NOTE: when running these modules locally, be sure to change USER to your BU Username
        and PASS to your BU Password
