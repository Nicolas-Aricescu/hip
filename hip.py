from tkinter.tix import MAX
import matplotlib.pyplot as plt 
import numpy as np



d = int(input('Enter d:'))
e = int(input('Enter e:'))

#cream coordonatele x si y 
x = np.linspace(-20, 20, 1000) 
y3 = np.sqrt((1/d*d)*(x**2) + e*e) 
y4 = -np.sqrt((1/d*d)*(x**2) + e*e) 

#desenam hiperbola
plt.plot(x, y3, color='blue', linewidth=2, label="hyperbola 1") 
plt.plot(x, y4, color='red', linewidth=2, label="hyperbola 2") 

#setam titlul si axele x si y
plt.title("Hyperbola") 
plt.xlabel('x') 
plt.ylabel('y') 

plt.axvline(0, color='black')
plt.axhline(0, color='black')
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Get user inputs
x1 = float(input('Enter the x-coordinate of the bottom left corner of the rectangle: '))
y1 = float(input('Enter the y-coordinate of the bottom left corner of the rectangle: '))
x2 = float(input('Enter the x-coordinate of the top right corner of the rectangle: '))
y2 = float(input('Enter the y-coordinate of the top right corner of the rectangle: '))

# Plot the rectangle
plt.plot([x1, x2], [y1, y1], color='green')
plt.plot([x1, x2], [y2, y2], color='green')
plt.plot([x1, x1], [y1, y2], color='green')
plt.plot([x2, x2], [y1, y2], color='green')
x3=x1
y3 = np.sqrt((1/d*d)*(x3**2) + e*e) 
max_y=max(y1,y2)
min_y=min(y1,y2)
if y3<=max_y and y3>=min_y:
    plt.plot(x3,y3,'black',markersize=15)


x3=x2
y3 = -np.sqrt((1/d*d)*(x3**2) + e*e) 
max_y=max(y1,y2)
min_y=min(y1,y2)
if y3<=max_y and y3>=min_y:
    plt.plot(x3,y3,'black',markersize=15)
   



#arata legenda 
plt.legend() 

#arata planul
plt.show()

