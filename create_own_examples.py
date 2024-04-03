import os 
from math import *
import random 

# Simple example 1d f(x) = (x+1)^2 = x^2+2x+1 
def f(x):
    return (x+1)**2

# Simple example 1d f(x) = sin(x)**2
def g(x):
    return sin(x)**2

# Simple example 2d f(x,y) = x^2 + y^2
def h(x,y):
    return x**2 + y**2

# Simple Physics example E = mc^2
def E(m,c):
    return m*c**2

# Simple Physics example F_gx = m*g*sin(theta) 
def F_gx(m,g,theta):
    return m*g*sin(theta)

# Hard example 1d f(x) = (tan(x) + 1)^2 
def f_hard(x):
    return (tan(x)*cos(x) + 1)**2

# Hard example 1d f(x) = sin(x)**2 + cos(x)**2
def g_hard(x):
    return sin(x)**2 + cos(x)**2

# Hard example 2d f(x,y) = x^2 + y^2 + 2*x*y
def h_hard(x,y):
    return x**2 + y**2 + 2*x*y

# Hard Physics example E = m*c^2*gamma
def E_hard(m,c,gamma):
    return m*c**2*gamma

# Hard Physics example F_gx = m*g*(sin(theta)+cos(theta))
def F_gx_hard(m,g,theta):
    return m*g*(sin(theta)+cos(theta))

def create_file(function):
    NUMBER_of_SAMPLES = 100000 # 10^5

    dir_path = "hard_examples/"
    os.makedirs(dir_path, exist_ok=True)

    with open(dir_path+function.__name__, "w") as file:
        for _ in range(NUMBER_of_SAMPLES):
            string_data = ""
            var = []
            for variables in range(function.__code__.co_argcount):
                value = random.uniform(1,5)
                var.append(value)
                string_data += str(value) + " "
            string_data += str(function(*var)) + "\n"
            file.write(string_data)    
            
create_file(f_hard)
create_file(g_hard)
create_file(h_hard)
create_file(E_hard)
create_file(F_gx_hard)

print("Files created.")
