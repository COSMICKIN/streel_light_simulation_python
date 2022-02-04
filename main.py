#taking input

inpt= open("a.txt","r")
line1= inpt.readline()
inpt_lst= line1.split()
D= int(inpt_lst[0])  #D is Duration of simulation
I= int(inpt_lst[1])  #I is the no. of intersections
S= int(inpt_lst[2])  #S is the no. of streets
V= int(inpt_lst[3])  #V is the no. of cars
F= int(inpt_lst[4])  #F is the bonus point for each car that reaches its destination before time D


class street:
    def __init__(self,B,E,Name,L):
        self.Begin= B               #Intersection at the Beginning of street
        self.End= E                 #Intersection at the End of street
        self.Name= Name             #Name of the street
        self.L= L                   #Time taken to travel in the street

class car:
    def __init__(self,P,Path):
        self.P= P                   #No. of streets to travel through
        self.Path= Path             #List of streets to travel through

Streets= []
for i in range(S):
    line= inpt.readline()
    lst= line.split()
    Streets.append(street(int(lst[0]),int(lst[1]),lst[2],int(lst[3])))

Cars= []
for i in range(V):
    line= inpt.readline()
    lst= line.split()
    P= int(lst[0])
    Path= lst[1:P]
    Cars.append(car(P,Path))
    
