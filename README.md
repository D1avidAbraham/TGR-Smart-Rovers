# TGR-Smart-Rovers
By Default GPIO pins 0-8 pull high and GPIO 9-27 pull low 
This is a problem because the rover using pins 6,7, 9, and 19. If powered ON then the rover will drive (off the table). 


So run the pyhton file in to set this pins to low. Then you can wire the rover. Open a terminal and download the code from the repository. 

'''
git clone https://github.com/D1avidAbraham/TGR-Smart-Rovers.git
'''

Then run the python file to set all the pins to low. 

'''
python3 setLow.py
'''
