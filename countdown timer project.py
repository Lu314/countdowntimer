import time 

sec = int(input("how many seconds in the countdown?"))

for x in range(sec):
    print(str(sec -x) + "seconds remaining")
    time.sleep(1)
