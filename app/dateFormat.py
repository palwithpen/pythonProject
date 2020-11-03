import datetime


def getTime():
    f = datetime.datetime.now()
    print(f.strftime("%X") , f.strftime("%x"))

def filePath():
    f = input("Enter absolute path of file")
    print("Your file location is ", f.strip())