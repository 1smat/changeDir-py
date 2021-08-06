import datetime, os, time
import schedule #  $ pip install schedule 

def sorter():
    print('ever day')

    td = datetime.datetime.today()
    currentDate = td.strftime("%d.%m.%Y") # get current date 
    todayDate = currentDate  # set current date to today

    print(currentDate)

    if todayDate != currentDate:
        currentDate = td.strftime("%d.%m.%Y")
        print('if ishladi')
        os.rename('Kunlik', todayDate)
        os.mkdir('Kunlik')
        todayDate = currentDate
    	# changing folder's name  

sorter()     
schedule.every().day.at("01:00").do(sorter)


while True:
    schedule.run_pending()
    time.sleep(1)