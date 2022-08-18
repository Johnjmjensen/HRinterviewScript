from multiprocessing.resource_sharer import stop
import time
import datetime
import json
import codecs

# employees = [["E1645","Donald","O’Connell","DOCONN","RD812","21‑JUN‑14"],
# ["84321","Samuel","Grant","SAGRAN","IT50","13‑OCT‑08"],
# ["0928","Jennifer","Whalen","JEWHAL","1001","18‑FEB‑85"],
# ["E9876","Krzysztof","Schrøder","KRSCHR","EU2018","01‑JAN‑98"], 
# ["G3821","Ophelia","Aetós","OPAETO","EU2018","05‑NOV‑20"],
# ["85218","Noémie","Jean-Pierre","NOJEAN","EU1382","25‑MAY‑10"],
# ["Augtest","θωερτψυιοπασδφγηςκλζχξωβνμ!@#$%^&*","яшертиуіопасдфгчйклзхцвбнмм,./;:?","θωερτψяшертиуіо","QAfake123","12‑AUG-32"]
# ]
# employee = ["EMPLOYEE_ID","FIRST_NAME","LAST_NAME","EMAIL","DEPT_CODE","HIRE_DATE"]
with codecs.open("./input/employees.json",encoding='utf-8') as inputFile:
    fileContent = json.load(inputFile)
employees = fileContent

# employees.append(fileContent)
# print(employees)
# print(len(employees))

def lengthLimit(arr):
    if len(arr) != 6:
        return "the entry ".join(arr)+" has an incorrect length for array."

def dateclean(date):
    date.replace("-","‑")

def isDate(arr):
    try:
        time.strptime(arr[5].replace("-","‑"),"%d‑%b‑%y")
    except:    
        return "start date for ".join(arr)+" Is formatted incorrectly."

def getMonth(arr):
    month = time.strptime(arr[5].replace("-","‑"),"%d‑%b‑%y").tm_mon
    return month

def getCurrentMonth():
    currentMonth = datetime.date.today().month
    return currentMonth

def getYear(arr):
    year = time.strptime(arr[5].replace("-","‑"),"%d‑%b‑%y").tm_year
    return year

def getCurrentYear():
    currentYear = datetime.date.today().year
    return currentYear

def isStartMonth(arr):
    if getCurrentMonth()==getMonth(arr):
        return True

def getTenure(arr):
    tenure = getCurrentYear()-getYear(arr)
    return str(tenure)+" years employed"
# print(lengthLimit(["E1645","Donald","O’Connell","DOCONN","RD812","21‑JUN‑14","Too Long"]))
# print(lengthLimit(["Too Short"]))
# print(isDate(["E1645","Donald","O’Connell","DOCONN","RD812","21‑JUN‑14"]))
# print(isDate(["E1645","Donald","O’Connell","DOCONN","RD812","21‑06‑14"]))
# print(getMonth(["E1645","Donald","O’Connell","DOCONN","RD812","21‑JUN‑14"]))
# print(getCurrentMonth())
# print(getYear(["E1645","Donald","O’Connell","DOCONN","RD812","21‑JUN‑14"]))
# print(getCurrentYear())
# print(isStartMonth(["E1645","Donald","O’Connell","DOCONN","RD812","21‑JUN‑14"]))
# print(isStartMonth(["E1645","Donald","O’Connell","DOCONN","RD812","21‑AUG‑14"]))
# print(getTenure(["E1645","Donald","O’Connell","DOCONN","RD812","21‑JUN‑14"]))

def anniversaryEmployees(employees):
    for employee in employees:
        # print(employee[5]) #troubleshooting involved in keeping array format when ingesting from anoother file.
        try:
            lengthLimit(employee)
        except:
            fileName = "./output/error"+str(getCurrentMonth())+".txt"
            with codecs.open(fileName,"a",encoding='utf-8',) as outputFile:
                outputFile.write(employee+"Has incorrect array length.\n")
            continue          
        try:
            isDate(employee)
        except:
            fileName = "./output/error"+str(getCurrentMonth())+".txt"
            with codecs.open(fileName,"a",encoding='utf-8',) as outputFile:
                outputFile.write(employee+"Has a malformedd date, use format 'dd-MMM-yy'.\n")
            continue
            #reformatting makes function return redundent revisit.       
                 
        if isStartMonth(employee) == True:
            anniversaryEmployee = employee[1]+" "+employee[2]+" "+employee[4]+" "+getTenure(employee)
            # print(anniversaryEmployee)
            # return(anniversaryEmployee)
            fileName = "./output/Anniveries"+str(getCurrentMonth())+".txt"
            with codecs.open(fileName,"a",encoding='utf-8',) as outputFile:
                outputFile.write(anniversaryEmployee+"\n")
        
anniversaryEmployees(employees)

#TODO add copy protection against repeated runs.
#TODO improve error handling to actualy handle cases of too short and incorrect dates when ingesting from file. 

