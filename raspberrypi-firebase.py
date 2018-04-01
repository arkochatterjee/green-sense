import pyrebase
import serial
import time
k = 0

config = {
    "apiKey": "AAAAS5jDbs0:APA91bGaHI1TH-y1hqOSI1mJxGTThyVntfaORIqcjzPyWc1aP0rLBuFfdC9qFa9gmWlBBnQvILJvb_JPIkoXXziKmyW86fNKS-MeWQ2JYOypJ5BLOTyjmMBR5B-NCwmM2FBIUpmvjzWI",
    "authDomain": "green-sense.firebaseapp.com",
    "databaseURL": "https://green-sense.firebaseio.com",
    "storageBucket": "green-sense.appspot.com"
    }

firebase = pyrebase.initialize_app(config)

db = firebase.database()

sdata=serial.Serial("/dev/ttyACM0",9600)
sdata.baudrate=9600
i = 1
while i == 1:
    readdata=sdata.readline() 
    readdata=str(readdata)    ##readdata has the data
    data = {"Data": readdata}
    ti = data["Data"]
    ti = data["Data"]
    for j in range (0,len(ti)):
        if(ti[j] ==";"):
            tim = ti[(j+1):(j+4)]
    print(tim)
    while int(tim)> 60:
        k=k+1
        if k<60:
            break
    
    hrs = str(k)
    findata = readdata[2:24]+hrs
    da = {"Data1": findata}
    print(da)
    db.child("arduino").push(da)
    
            
import pyrebase
import serial
import time
k = 0

config = {
    "apiKey": "AAAAS5jDbs0:APA91bGaHI1TH-y1hqOSI1mJxGTThyVntfaORIqcjzPyWc1aP0rLBuFfdC9qFa9gmWlBBnQvILJvb_JPIkoXXziKmyW86fNKS-MeWQ2JYOypJ5BLOTyjmMBR5B-NCwmM2FBIUpmvjzWI",
    "authDomain": "green-sense.firebaseapp.com",
    "databaseURL": "https://green-sense.firebaseio.com",
    "storageBucket": "green-sense.appspot.com"
    }

firebase = pyrebase.initialize_app(config)

db = firebase.database()

sdata=serial.Serial("/dev/ttyACM0",9600)
sdata.baudrate=9600
i = 1
while i == 1:
    readdata=sdata.readline() 
    readdata=str(readdata)    ##readdata has the data
    data = {"Data": readdata}
    ti = data["Data"]
    ti = data["Data"]
    for j in range (0,len(ti)):
        if(ti[j] ==";"):
            tim = ti[(j+1):(j+4)]
    print(tim)
    while int(tim)> 60:
        k=k+1
        if k<60:
            break
    
    hrs = str(k)
    findata = readdata[2:24]+hrs
    da = {"Data1": findata}
    print(da)
    db.child("arduino").push(da)
    
            

