# -*- coding: utf-8 -*-
"""
Main script for triggering sunset / sunrise features
@author: Niels Petersen
"""
import warnings
import lights
from gpizero import Button

button1 = None
controller = lights.TrafficSignal()

def initializeButton():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #GPIO.add_event_detect(12, GPIO.RISING, callback=stopSunrise, bouncetime=250)

def main():
    
    # Setup button to detect press events to show traffic lights
    initializeButton()

if __name__ == "__main__":
    warnings.filterwarnings('ignore')
    main()