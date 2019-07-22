# In the first type of the method
# We have both input and output values

def cylinder_volume(radius,height):
	return 3.14*radius*radius*height

# In second type of method we won't take any input 
# and we won't give any output

def greeting():
	print("Hi I am a function")

# In third type of method we will take a input
# but we won't give any output

def area_circle(radius):
	area = 3.14*radius**2
	print("The area of the circle is: ",area)


a = cylinder_volume(10,10)

greeting()

area_circle(20)











