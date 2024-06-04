import pywhatkit as kit
import pyautogui as auto
import schedule
from time import *
import sys

def Gm(phone,msg,time1,min):
    i = 0
    for i in range(len(phone)):
        kit.sendwhatmsg(phone[i],msg,time1,min)
        auto.press("Enter")
        min += 1
        if (len(phone)) == i:
            exit()
    
def main():
    phone = ["+919860293951","+919750055591","+919112743571"]
    msg = "*Jay Shree Ram 🙏.*"
    while True:
        schedule.every(1).day.do(Gm(phone,msg,int(sys.argv[1]),int(sys.argv[2])))
        
        schedule.run_pending()
        sleep(1)

if __name__ == "__main__":
    main()
    


    

