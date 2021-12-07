
# Task 1---------------------------------
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  

print("Prime numbers between", lower, "and", upper, "are:") 
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num) 
# Task 2-------------------------
def showStudent(name,GPA=0):
    print(name,GPA)


showStudent ("Omar",3)

# Task3----------------------------

subjects_grades = { 'Physics': 90, 'Math': 100, 'history': 70 }
print("Minimum grade is: "+min(subjects_grades ,key =subjects_grades.get))
print("Maximum grade is: "+max(subjects_grades,key=subjects_grades.get))

