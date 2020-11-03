import datetime


def getTime():
    f = datetime.datetime.now()
    print(f.strftime("%X") , f.strftime("%x"))