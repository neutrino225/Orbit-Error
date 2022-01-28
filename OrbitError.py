#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 02:50:49 2022

@author: neutrino
"""

import math
import numpy
import matplotlib.pyplot

# These are used to keep track of the data we want to plot
h_array = []
error_array = []

total_time = 24. * 3600. # s
g = 9.81 # m / s2
earth_mass = 5.97e24 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2
radius = (gravitational_constant * earth_mass * total_time**2. / 4. / math.pi ** 2.) ** (1. / 3.)
speed = 2.0 * math.pi * radius / total_time

def acceleration(spaceship_position):
    vector_to_earth = - spaceship_position # earth located at origin
    return gravitational_constant * earth_mass / numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth

def calculate_error(num_steps):
    h = total_time / num_steps
    x = numpy.zeros([num_steps+1,2])
    v = numpy.zeros([num_steps+1,2])
    
    x[0,0] = radius     # initial distance
    v[0,1] = speed      # initial speed
    
    for i in range(num_steps):      # Using foward Euler method to calculate distance and velocity
        x[i+1] = x[i] + h * v[i]                
        v[i+1] = v[i] + h * acceleration(x[i]) 
        
    error = numpy.linalg.norm(x[-1] - x[0])     # calculating the difference between the initial and the final position
    # This is used for plotting
    h_array.append(h)
    error_array.append(error)
    return error
    
h_array=[]
error_array=[]
for num_steps in [200, 500, 1000, 2000, 5000, 10000]:
    error = calculate_error(num_steps)

def plot_me():
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Step size in s')
    axes.set_ylabel('Error in m')
    matplotlib.pyplot.scatter(h_array, error_array)
    matplotlib.pyplot.xlim(xmin = 0.)
    matplotlib.pyplot.ylim(ymin = 0.)

plot_me()
