class People:
    
    def numberOfCoures ():
        return int(input ("Enter the number of the course: "))

numberStudent= int(input("Enter the number of student want to enter: "))
#ham nhap
def InformationofStudent():
    listst= []
    for b in range(0,numberStudent,2):
        nameofSt = input("Name:")
        listst.append(nameofSt)
        print("-"*50)
        idofSt =input("ID:")
        listst.append(idofSt)
        print("-"*50)
        DobOfSt = input("Dob:")
        listst.append(DobOfSt)
        print("-"*50)
    return listst

listst = InformationofStudent()
def ListSt(listst):
    for i in range(0,numberStudent,3):
        print("Name: ", listst[i])
        print("-"*50)
        print("ID: ", listst[i+1])
        print("-"*50)
        print("Dob: ", listst[i+2])
      
print(ListSt(listst))



#ham xuat
number = int(input("Number of Course: "))
#Ham nhap
def CoursesInfomation():
     list = [] 
     for u in range (number):
        idOfcourses = input("Enter Id the courses:")
        list.append(idOfcourses)
        nameOfcourses = input("Enter the name of the course: ")
        list.append(nameOfcourses)
     return list
list = CoursesInfomation()
#Ham xuat
def ListFunction(list):
    for i in range(0,number,2):
        print("ID: ", list[i])
        print("-"*50)
        print("Name: ", list[i+1])
print(ListFunction(list))
   

def Mark(idOfcourses,idofSt):
   
        prompt = f"Enter marks of {idofSt} for course   {idOfcourses}: ".format (idofSt, idOfcourses)
        input (prompt)
listmark= []




print(InformationofStudent())
print(numberOfCoures())
print(CoursesInfomation())
mark1 = int(input())
mark2 = int(input())
print(Mark(mark1,mark2))
print(ListFunction(list))