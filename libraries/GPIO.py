from RPi.GPIO import GPIO

class myGPIO :
    def __init__(self, play_pause_pin = None, next_pin=None, prev_pin=None):
        # Définir les broches GPIO sur lesquels sont branchés les boutons
        self.play_pause_pin = play_pause_pin
        self.next_pin       = next_pin
        self.prev_pin       = prev_pin


    def set_pins(self, play_pause_pin, next_pin, prev_pin):
        # Définir les broches GPIO sur lesquels sont branchés les boutons
        self.play_pause_pin = play_pause_pin
        self.next_pin       = next_pin
        self.prev_pin       = prev_pin

        if (self.play_pause_pin == None) or (self.next_pin == None) or (self.prev_pin == None):
            print("GPIO pins not set")
            exit(-1)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.next_pin,       GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.prev_pin,       GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.play_pause_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    def set_callbacks(self, video_manager):
        # Définir les fonctions de callback pour chaque bouton
        GPIO.add_event_detect(self.next_pin,       GPIO.FALLING, callback=video_manager.next,       bouncetime=300)
        GPIO.add_event_detect(self.prev_pin,       GPIO.FALLING, callback=video_manager.previous,   bouncetime=300)
        GPIO.add_event_detect(self.play_pause_pin, GPIO.FALLING, callback=video_manager.play_pause, bouncetime=300)

    def cleanup(self):
        GPIO.cleanup()
