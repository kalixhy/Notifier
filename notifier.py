

#for getting notification on your PC
from plyer import notification 

notification.notify(
    
        #title of the notification,
        title = "Code Reminders",
        #the body of the notification
        app_name = "Notifier",

        message = "do a machine learning project  😂😂😂",  
        #creating icon for the notification
        #we need to download a icon of ico file format
       app_icon = "./icon/icon.ico",
        # the notification stays for 15sec
        timeout  = 15
)
