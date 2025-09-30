import RPi.GPIO as GPIO

# Set the mode to BCM
GPIO.setmode(GPIO.BCM)

# Set pins 6,7, 9, and 19 to low 
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(9, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)

