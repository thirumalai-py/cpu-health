import psutil
from playsound import playsound

"""
Script to monitor CPU health in mac or windows local machine and raise sound if exceeds the threshhold
"""

# CPU Threshold
CPU_THRESHOLD = 70
ALERT_SOUND = "/media/alert.mp3"
INTERVAL = 2 # Sets the time interval on which the psutil has to check the cpu_percent

while True:
    try:
        cpu_usage = psutil.cpu_percent(INTERVAL) # interval in seconds
        if cpu_usage <= CPU_THRESHOLD:
            print(f"Monitoring CPU Usage...Current utilisation: {cpu_usage}%")
        else:
            memory_info = psutil.virtual_memory()
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}% | Memory Usage: {memory_info.percent}% ")
            playsound(ALERT_SOUND) # Play Sound 

    except Exception as e:
        print(f"Error occurred: {e}")
        break  # Exit the loop if an error occurs
