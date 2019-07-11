#basics1 
pi = 22/7

radian = 32*(pi/180) #this converts 32 degrees to radian
print(radian) #this prints out the radian

#this is for basics 2

r= input("Please  input the raduis of your sphere") #this ask the user to input the radius
d = float(r)
rr =d*d #this squares the raduis
rrr = d*d*d

surface_area = 4*pi*rr
print("the surface area is ", surface_area) #  this prints out the surface area
volume = (4/3)*pi*rrr
print("the volume is ", volume) #  this prints out the volume


#basics3

from datetime import datetime
now = datetime.now()
dt_strig = now.strftime("%H:%M")
print("the time is = ",dt_strig )
print(now)


