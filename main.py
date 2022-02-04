#taking input

inpt= open("a.txt","r")
line1= inpt.readline()
inpt_lst= line1.split()
D= inpt_lst[0]  #D is Duration of simulation
I= inpt_lst[1]  #I is the no. of intersections
S= inpt_lst[2]  #S is the no. of streets
V= inpt_lst[3]  #V is the no. of cars
F= inpt_lst[4]  #F is the bonus point for each car that reaches its destination
