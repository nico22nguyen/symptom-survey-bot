# ss_bot
  - logs into patient connect
  - completes daily BU symptom survey screening
  - also serves as helper module for daily_pc_bot
  
# apt_maker
  - provides appointment scheduling functionality for daily_pc_bot
 
# daily_pc_bot
  - 1 stop shop for all things patient connect (to be run daily)
  - logs into patient connect
  - completes symptom survey
  - determines if/when an appointment needs to be scheduled
  - if the bot finds that you have no appointment, it schedules one on the proper day
  - Note: default appointment time = "1:00", default appointment location = "agganis"
          to change these, simply change the values passed into apt_maker()
          
  NOTE: when running these modules locally, be sure to change USER to your BU Username
        and PASS to your BU Password
