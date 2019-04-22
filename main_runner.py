from Modules_Packages.aadhar_project import Options as o1
import datetime
t=datetime.datetime.today()
print("WELCOME TO ADDHAR SYSTEM" + "            " + str(t))
print("---------------------------------------------------------------")
flagc='Y'
while (flagc=='Y'): 
    print("choose your option ")
    print("------------------")
    print("1. open an aadhar")
    print("2. update aadhar information")
    print("3. enquire aadhar information")
    print("4. continue aadhar registration using token number")
    print("5. everify aadhar")
    op=int(input("enter your option [1,2,3,4,5]: "))
    flagop='N'
    if op not in [1,2,3,4,5]:
        t=datetime.datetime.today()
        print("invalid option.You have successfully exited aadhar system at " + str(t))
        flagop='N'
        break
    else:
        flagop='Y'
    
    if flagop=='Y':
        o1.func(op)
    a=input("do you want to continue (Y/N) for next enquiry in aadhar system? ")
    if a=='Y':
        continue
    else:
        flagc='N'
        t=datetime.datetime.today()
        print("You have successfully exited aadhar system at " + str(t))
        


