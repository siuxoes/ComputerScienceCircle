__author__ = 'Siuxoes'

time = str(input())
minutes = int(input())

doublePoints = time.index(":")
hours = time[:doublePoints]
minutes2 = time[(doublePoints+1):]
secondsTotal = int(hours)*3600 + int(minutes2)*60 + int(minutes)*60
import time
print(time.strftime('%H:%M', time.gmtime(secondsTotal)))