# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:10:42 2020

@author: karel
"""

def calc_weight_on_planet(weight, surf_grav=23.1):
    mass = weight/9.8
    return mass*surf_grav

print(calc_weight_on_planet(120))