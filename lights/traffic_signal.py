#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 10:48:58 2024

@author: Niels Petersen
"""

import time
import board
from gpiozero import LED

class TrafficSignal:
    __instance = None
    
    @staticmethod
    def getInstance():
        if TrafficSignal.__instance != None:
            TrafficSignal()
        return TrafficSignal.__instance
    
    def __init__(self, ):
        
        red_light = LED(2) #GPIO 2 
        yellow_light = LED(3) #GPIO 3
        green_light = LED(4) #GPIO 4
        
        
        
        
        
        
        
        
        
        