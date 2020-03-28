from datetime import datetime
import psutil as p
import schedule
import time
second = int(input("Enter second: "))
time_ = input('Enter time: ')

def job():
    for i in range(second):
        f = open('schedule', 'a')
        cpu=p.cpu_percent(interval=1)
        print(cpu)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        #print("Current Time =", current_time)
        f.write(current_time + "," + str(cpu) + "\n")
        f.close()
schedule.every().day.at(time_).do(job)

#schedule.every().day.at(time_).do(job)
while True:
    schedule.run_pending()
    time.sleep(1)


