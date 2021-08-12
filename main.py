import datetime, os, time
import schedule #  $ pip install schedule 

currentDate = datetime.datetime.today().strftime("%d.%m.%Y")  # get current date
todayDate = currentDate

print('todayDate ' + todayDate)
print('currentDate: ' + currentDate)

def sorter():
    global todayDate, currentDate

    if todayDate != datetime.datetime.today().strftime("%d.%m.%Y"):
        currentDate = datetime.datetime.today().strftime("%d.%m.%Y")
        print('Changing dir names...')
        os.rename('Kunlik', todayDate)
        os.mkdir('Kunlik')
        todayDate = currentDate
        print('todayDate: ' + todayDate)
        print('currentDate: ' + currentDate)
    	# changing folder's name 

schedule.every().day.at("00:00").do(sorter)

while True:
    schedule.run_pending()
    time.sleep(1)
