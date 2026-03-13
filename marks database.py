

n =int(input("enter the number of students:"))
   
def input_marks():
    noofsubjects = int(input("enter the no of subjects:"))
    for j in range(noofsubjects):
        subject = input("enter the subject name:")
        marks = int(input("enter the marks:"))
       
    if (marks < 0 and marks > 100):
        print("marks not proper format")
    else:
        student[subject] = marks
    return(student) 
                   

def calculate_marks(student):
    mark = student.values()
    s = sum(mark)
    avg = s/len(student) 
    h = max(mark)
    l = min(mark)
 
    return s,avg,h,l

def output_marks(avg):
    if(avg > 40):
        print("result:pass")
    else:
        print("result:fail")

def results(name,student,s,avg,h,l):
    print("student name=",name)
    for subject, mark in student.items():
     print(subject, ":", mark) 
    print("sum=",s)
    print("average=",avg)
    print("highest=",h)
    print("lowest=",l)

for i in range(n):
    student ={}
    name = input("enter the name of the student:")
    noofsubjects= input_marks()
    s,avg,h,l = calculate_marks(student)
    results(name,student,s,avg,h,l)
    output_marks(avg)
    