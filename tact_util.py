#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    
'''

# Import necessary modules

def get_country_details(name):    

    country_details = {
        "name" : "N/A",
        "capital_city" : "N/A",
        "population_in_millions" : "N/A"
    }

    if(name == 'canada'):
        country_details = {
            "name" : "Canada",
            "capital_city" : "Ottawa",
            "population_in_millions" : 36.71
        }
    elif (name == 'india'):
        country_details = {
            "name" : "India",
            "capital_city" : "New Delhi",
            "population_in_millions" : 1339
        }

    return country_details

if __name__ == '__main__':
    pass

