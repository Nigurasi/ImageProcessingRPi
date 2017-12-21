import threading
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class Button(threading.Thread):
    
    states = []
    def __init__(self, channel, channelBack, red_channel, green_channel, blue_channel):
        threading.Thread.__init__(self)
        self._pressed = False
        self.channel = channel
        self.channelBack = channelBack
        self.button_state = 0
        self.state = True;
        GPIO.setup(self.channel, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.channelBack, GPIO.IN, GPIO.PUD_UP)
        # GPIO.setup(red_channel, GPIO.OUT)
        # GPIO.setup(green_channel, GPIO.OUT)
        # GPIO.setup(blue_channel, GPIO.OUT)
        # self.states.append([])
        # self.states.append([])
        # self.states.append([])
        # self.states.append([red_channel])
        # self.states.append([red_channel, green_channel])
        # self.states.append([green_channel])
        # self.states.append([green_channel, blue_channel])
        # self.states.append([blue_channel])
        # self.states.append([red_channel, blue_channel])
        # self.states.append([])
        
        # GPIO.output(red_channel, 0)
        # GPIO.output(green_channel, 0)
        # GPIO.output(blue_channel, 0)
        
        print("Starting...")
        self.start()
        
    def run(self):
        previous = 1
        previousBack = 1
        while self.state:
            current = GPIO.input(self.channel)
            currentBack = GPIO.input(self.channelBack)
             
            if current == 0 and previous == 1:
                self._pressed = True
                 # for led in self.states[self.button_state]:
                     # GPIO.output(led, 0)
                self.button_state = (self.button_state+1)%9
                
                 # for led in self.states[self.button_state]:
                     # GPIO.output(led, 1)
                print("pressed")
            
            if currentBack == 0 and previousBack == 1:
                self._pressed = True
                
                if self.button_state - 1 < 0:
                    self.button_state = 8
                else:
                    self.button_state = (self.button_state-1)%9

                print("Back")
            previous = current
            previousBack = currentBack
            
            
            time.sleep(0.01)
             
    def onButtonPress():
        print("pressed")