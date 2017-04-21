import RPi.GPIO as GPIO

class Team:
    def __init__(self, button, led_self, led_op, name):
        self.button = button
        self.led_self = led_self
        self.led_op = led_op
        self.name = name

#define the teams
#TODO: SWITCH THE PINS(2 AND 3 ALREADY HAVE PULL UP RESISTORS)
judge = Team(1, 1, 1, "JUDGE")
huberts = Team(2, 2, 2, "HUBERTS")
ryan = Team(3, 3, 3, "RYAN")
flower = Team(4, 4, 4, "FLOWER")

#gather our teams
teams = [judge, huberts, ryan, flower]

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
for team in teams:
    GPIO.setup(team.button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(team.led_self, GPIO.OUT)
    GPIO.setup(team.led_op, GPIO.OUT)

def execute_game():
    #run game loop
    while True:
        try:
            input_state = GPIO.input(team.button)
            if(input_state == True):
                buzzed_team = team
                GPIO.output(team.led_table, HIGH)
                #temporarily print to the terminal
                print("GOT TEAM INPUT FROM: " + buzzed_team = team);
        except KeyboardInterrupt:
            exit()
