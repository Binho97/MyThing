def get_hour_worked():
    x=int(input("Enter No of hour Worked by an employee:"))
    return x

def get_hourly_rate():
    x=int(input("Enter any employee's hourly rate:"))
    return x

def get_input():
    worked_hour=get_hour_worked()
    hourly_rate=get_hourly_rate()
    return [worked_hour,hourly_rate]

def calc_gross_pay(a,b,c):
    return a*b+c

def calc_overtime_pay(b):
    overtime=int(input("Enter No of Overtime Hours worked:"))
    
    return overtime*b

def calc_withholdings(n):
    
    return n*3//100

def calc_net_pay(gross_pay,withholdings):
    return gross_pay-withholdings

def printout(net_pay):
    print("total Paid to Employee:",net_pay)

arr=get_input()
hours=arr[0]
rate=arr[1]
overtime_pay=calc_overtime_pay(rate)
gross_pay=calc_gross_pay(hours,rate,overtime_pay)
withholdings=calc_withholdings(gross_pay)
net_pay=(gross_pay - withholdings)
printout(net_pay)
