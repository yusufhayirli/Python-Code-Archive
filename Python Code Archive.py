
"""
##################################################
##################################################
############## REGULAR CODES #####################
##################################################
##################################################

# Area of 2 square at around a circle --->>>

radius=int(input("Enter radius"))
innersquare=((radius*2)/(2**0.5))
outersquare=radius*2
areainner=innersquare**2
areaouter=outersquare**2
print(areainner)
print(areaouter)
"""

# ABSOLUTE NUMBER --->>>
"""
x=int(input("Enter a number"))
if x<0:
    x=-x
print(x)
"""


# TICKET PRICE --->>>
"""
price=3
age=int(input("Enter your age"))
if age<6 or age>18:
    print("You do not have to pay")
elif age>=6 and age<=18:
    print(price*0.50)
else:
    print(price)
"""   
# SEASON SECTIONs --->>>
"""
month=input("Enter the current month: ")
day=int(input("Enter the current day: "))

Season="Your entries are not valid."

if month=="January" or month=="February":
    Season="Winter"
elif month=="April" or month=="May":
    Season="Spring"
elif month=="July" or month=="August":
    Season="Summer"
elif month=="October" or month=="November":
    Season="Fall"
if month=="March":
    if day>=20:
        Season="Spring"
    else:
        Season="Winter"
elif month=="June":
    if day>=21:
        Season="Summer"
    else:
        Season="Spring"
elif month=="September":
    if day>=22:
        Season="Fall"
    else:
        Season="Summer"
elif month=="December":
    if day>=21:
        Season="Winter"
    else:
        Season="Fall"
        
print("Your current season is",Season)
"""
#################################

# Try / Except - if/else

################################# 26.10.2018
"""
try:
    num=input("Enter a number or word: ")
    num=int(num)
    if num%2==0:
        print(num*10)
    else:
        print(num*20)
except:
    try:
        num=float(num)
        print(round(num))
    except:
        if len(num)%2==0:
            print(num.upper())
        else:
            print(num.lower())
"""
###################################################################
"""
gpa=float(input("Enter your GPA: "))
lects=int(input("How many lectures you took? : "))
if gpa<2.0 and lects<47:
    print("You've failed this city !")
elif gpa>=2.0 and lects<47:
    print("Your have not enough credits.")
elif gpa<2.0 and lects>=47:
    print("Your GPA is not enough !")
else:
    print("Conguratulations!\nYou are Graduated.")
"""
###################################################################
"""
a=int(input("Enter your a component: "))
b=int(input("Enter your b component: "))
c=int(input("Enter your c component: "))

delta=(b**2)-4(a*c)
if delta>0:
    r1=((-b)+(delta**0.5))/(2*a)
    r2=((-b)-(delta**0.5))/(2*a)
    print("You have two real roots as:",r1,"and",r2)
elif delta==0:
    r1=((-b)+(delta**0.5))/(2*a)
    print("You have only one root as:",r1)
else:
    print("You have no roots.")
"""

#################################
"""
##################################################
##################################################
################# FOR LOOPS ######################
##################################################
##################################################
"""
################################# 02.11.2018


"""
for i in range(10):
    print("Hello")
print("Good Bye!")
"""
###################################################################
"""
for i in range(17):
    print(i)
"""
###################################################################
"""
for i in range(2,17):
    print(i+0.5)
"""
###################################################################
"""
for i in range(2,17,3):
    print(i)
"""
###################################################################
"""
movie_list=["Mad Max", "Interstellar", "Taxi Driver", "Whiplash", "The Prestige"]

for i in range(len(movie_list)):
    print(movie_list[i])
"""
###################################################################
"""
for movie in movie_list:
    print(movie)
"""
###################################################################
"""
name="Yusuf"
for char in name:
    print(char)
"""
###################################################################
"""   
sums=0
nums=[8,60,43,55,25,134,1]
for i in nums:
    sums+=i
print(sums)
"""
###################################################################
"""
power_a=1
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

if b>0:
    for i in range(b):
        power_a*=a
    print(power_a)
else:
    for i in range(0,b,-1):
        power_a/=a
    print(power_a)
"""
###################################################################
"""
factorial=1
n=int(input("Enter a number: "))
for i in range(n,1,-1):
    factorial*=i
print(factorial)
"""
###################################################################
"""
sum_of_digits=0
pos_int=input("Enter your number: ")
for digit in pos_int:
    sum_of_digits+=int(digit)
print(sum_of_digits)
"""
###################################################################
"""
a=0
b=1
x=int(input("How many number do you want? "))
for i in range(x):
    c = a
    a = b
    b = c + b
    print(a)
"""
###################################################################

### Yusuf HAYIRLI - 240201130 ### 09.11.2018
"""
nums=[8,60,43,55,25,134,1]
a=0
i=0
while i<len(nums):
    a+=nums[i]
    i+=1
print(a)
"""
###################################################################
"""
##################################################
##################################################
################ WHILE LOOPS #####################
##################################################
##################################################
"""

"""
while True:
    a=int(input("Enter your first number: "))
    b=int(input("Enter your second number: "))
    if a>b:
        temp=b
        b=a
        a=temp
    check=a
    while a>0 and b>0:
        if (b%check) ==0 and (a%check==0):
            print("Your GCD is:",check)
            break
        else:
            check-=1
            if check==1:
                print("Your GCD is: 1")
    break
"""
###################################################################
"""

name=""
idd="1"
while True:
    idd=str(idd)
    name=input("Enter name:")
    try:
        name=int(name)
        if name==0:
            break
    except:
        salar=int(input("Enter Salary:"))
        salary=str(salary)
        dep_of_emp=input("Enter Department:")
        file=open("Employee.txt","a")
        file.write(idd+" "+name+" "+salary+" "+dep_of_emp+"\n")
        file.close()
    idd=int(idd)
    idd+=1
file=open("Employee.txt","r")
a=file.readlines()
print(a)

"""
"""
##################################################
##################################################
################### FILES ########################
##################################################
##################################################
"""
"""
A=[[0 for col in range(3)] for row in range(3)]
B=[[0 for col in range(3)] for row in range(3)]
file.open("matrices.txt","r")
lines=file.readlines()
for line in lines:
    if line.strip()=="matrix A" or line.strip()=="matrix B":
        continue
    line=line.split()
    row=0
    for i in range(len(line)):
        A(row)[i]=int(line[i])
        row+=1
"""
###################################################################
"""
file=open("matrices.txt","r+")

A=[[0 for col in range(3)] for row in range(3)]
B=[[0 for col in range(3)] for row in range(3)]
SUM=[[0 for col in range(3)] for row in range(3)]
for line in file.readlines():
    info=line.split()
    if info[0]=="matrix":
        i=0
        matrix_id=info[1]
        continue
    else:
        for j in range(0,3):
            if matrix_id=="A":
                A[i][j]=int(info[j])
            else:
                B[i][j]=int(info[j])
        i+=1

for i in range(0,3):
    for j in range(0,3):
        SUM[i][j]=A[i][j]+B[i][j]

print(SUM)
"""
"""
file.write("\n")
file.write("Matrix Sum\n")
for i in range(0,3):
    for j in range(0,3):
        SUM[i][j]=A[i][j]+B[i][j]
        file.write(str(SUM[i][j])+" ")
    file.write("\n")
print(SUM)
"""
# Yusuf HAYIRLI - 240201130 / 07.12.2018
"""
##################################################
##################################################
################# FUNCTIONS ######################
##################################################
##################################################
"""
"""
1- No Parameter + No return
def print_random_area():
    print(3.14*(random.randint(5,20)**2))
    
2- Parameter + No return
def print_area(radius):
    print(3.14*(radius**2))

3- Default parameter + No return
def print_area(radius=10):
    print(3.14*(radius**2))

4- Parameter + Return
def get_area(radius):
    return 3.14*(radius**2)

5- No parameter + Return
def get_random_area():
    return (3.14*(random.randint(5,20)**2))
"""
########################################################################
"""
def print_area(r):
    print(3.14*r*r)
    
def cube(x):
    return x*x*x

def main():
    print_area(10) # Functional call 2
    print(cube(3)) # Functional call 3 and 4
    
main() # Functional call 1
"""
########################################################################
"""
def is_prime(n):
    if n < 2:
        return(False) # why not using else ?
        
    for i in range(2,n//2): # why not range(2,n) ?
        if (n%i)==0:
            return(False)
        else: # not necessary
            continue
    return(True)

def print_primes_between(b,e):
    for i in range(b,e):
        if is_prime(i):
            print(i)

def main():
    x=int(input("begin? "))
    y=int(input("end? "))
    print_primes_between(x,y)
    
main()

def is_primee(x): # mine and simple.
    for i in range(2,x):
        if x%i==0:
            return False
    return True

"""
########################################################################
"""
import random
random.seed(12)
def get_rand_list(a,b,N):
    ListA=[]
    for i in range(N):
        ListA.append(random.randint(a,b))
    return ListA

def get_overlap(x,y):
    z=[]
    for i in x:
        if i in y:
            z.append(i)
    return z

def main():
    a=0
    b=10
    N=5
    x=get_rand_list(a,b,N)
    y=get_rand_list(a,b,N)
    z=get_overlap(x,y)
    print(x)
    print(y)
    print(z)
    
main()
"""

"""
##################################################
##################################################
################# DICTIONARYS ####################
##################################################
##################################################
"""
"""
books=["ULYSSES","ANIMAL FARM","BRAVE NEW","ENDER'S GAME"]

def construct_dict(books):
    book_dict={}
    for i in range(len(books)):
        book_dict.update({books[i]:(len(books[i]),len(set(books[i])))})
    return book_dict
    
def print_dict():
    x=construct_dict(books)
    for i in x:
        print(i,"->",x[i])
        
def update_dict(x):
    for i in x:
        x.update({i:(x[i][0],x[i][1],int((x[i][0]+x[i][1])/2))})
        print(i,"->",x[i])
        
print_dict()
print("########### UPDATED #############")
update_dict(construct_dict(books))
"""

"""
##################################################
##################################################
#################### SETS ########################
##################################################
##################################################
"""
"""
numbers1=[2,3,4,20,5,5,15]
numbers2=[10,20,20,15,30,40]

def unique_list(alist):
    alist=set(alist)
    alist=list(alist)
    return alist
print("##########################################")
print("Unique 1:",unique_list(numbers1))
print("Unique 2:",unique_list(numbers2))

def intersection(alist,blist):
    alist=set(alist)
    blist=set(blist)
    clist=set([])
    for i in alist:
        if i not in blist:
            clist.add(i)
    return list(clist)

def union(alist,blist):
    alist=set(alist)
    blist=set(blist)
    clist=set([])
    for i in alist:
        if i in blist:
            clist.add(i)
    return list(clist)
print("##########################################")
print("Intersection:",intersection(numbers1,numbers2))
print("Union:",union(numbers1,numbers2))
"""

"""
##################################################
##################################################
################# RECURSIONS #####################
##################################################
##################################################
"""
"""

def itr_fact(n): ### Factorial with For
    result=1
    for i in range(2,n+1):
        result*=i
    return result

def rec_fact(n): ### Factorial with Recursion
    if n==1:
        return 1
    else:
        return n * rec_fact(n-1)
    
print(itr_fact(5))
print(rec_fact(5))

summm=0
def harmonic(n): ### 1 + 1/2 + 1/3 + 1/n
    if n==1:
        return 1
    else:
        return 1/n + harmonic(n-1)

print(harmonic(3))

mylist=[1,2,3,4,6,10,12,16,7,5,3]

def get_reversed(alist): ### Reverses the list
    if len(alist)==1:
        return alist
    else:
        return alist[-1:] + get_reversed(alist[:-1])
    
print(get_reversed(mylist))

summm=0
def even_of_list(alist): ### Even of list's count
    if len(alist)==0:
        return 0
    else:
        if alist[0]%2==0:
            return 1 + even_of_list(alist[1:])
        else:
            return even_of_list(alist[1:])

print(even_of_list(mylist))

import time #####

def counter(t): ### TIMER 30 Sec to 0
    if t==0:
        return 0
    else:
        print(t)
        time.sleep(1)
        counter(t-1)
        
counter(30)

"""
"""
### Counts symbols in given string ###
def count_specials(str): 
    if len(str)<1:
        return 0
    else:
        if not (str[0].isalpha() or str[0].isdigit()):
            return 1 + count_specials(str[1:])
        else:
            return count_specials(str[1:])


### Reverse the given list ###
def reverse(a): 
    if len(a) == 1:
        return a
    else:
        return [a.pop()] + reverse(a)

### Finds sum of simple list ###
def find_sum_a_list(xlist):
    if len(xlist) == 0 :
        return 0
    else:
        return xlist[0] + find_sum_a_list(xlist[1:])


### Finds sum of nested lists ###
def find_sum_nested_lists(x):
    if len(x) == 0 :
        return 0
    else:
        if not isinstance(x[0], list):
            return x[0] + find_sum_nested_lists(x[1:])
        else:
            return find_sum_nested_lists(x[0]) + find_sum_nested_lists(x[1:])


### Returns last line of Pascal Triangle for given sequence of integer ###
def pascal_triangle_last_line(n):
    if n == 1:
        return [1]
    else:
        x = pascal_triangle_last_line(n-1)
        y = []
        y.append(1)
        for i in range(len(x) -1):
            y.append(x[i] + x[i+1])
        y.append(1)
        
        return y

### Returns all lines of Pascal Triangle for given sequence of integer ###
def pascal_triangle(n):
    if n == 1:
        return [[1]]
    else:
        all_lines = pascal_triangle(n-1)
        x = all_lines[-1]
        
        y = []
        y.append(1)
        for i in range(len(x) -1):
            y.append(x[i] + x[i+1])
        y.append(1)
        
        all_lines.append(1)
        return all_lines

print("########### Count Specials ###########")
print(count_specials("gfsd+^%^+%+"))
print("########### Reverse List ###########")
print(reverse([3,4,6]))
print("########### Single List Sum ###########")
print(find_sum_a_list([2,3,4]))
print("########### Nested List Sum ###########")
print(find_sum_nested_lists([1,2,[4,5,2,[4,5]],7,10]))
print("########### Pascal Triangle Last ###########")
print(pascal_triangle_last_line(5))
print("########### Pascal Triangle ###########")
print(pascal_triangle(5))
"""