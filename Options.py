from Modules_Packages.aadhar_project import Option1 as o1
from Modules_Packages.aadhar_project import Option2 as o2
from Modules_Packages.aadhar_project import Option3 as o3
from Modules_Packages.aadhar_project import Option4 as o4
from Modules_Packages.aadhar_project import Option5 as o5
def func(op):
    if op==1:
        z=o1.validation.funcvalidation()
        if z[0]==10:
            o1.pandb(z[1],z[2],z[3],z[4],z[5],z[6],z[7]).read_pandb()
            return
        else:
            print(z)
    elif op==2:
        print(o2.func())
    elif op==3:
        print(o3.func())
    elif op==4:
        print(o4.func())
    elif op==5:
        print(o5.func())
    else:
        print("invalid option")


