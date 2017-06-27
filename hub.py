import pyrebase as fb
import RPi.GPIO as io
import time

io.setmode(io.BOARD)

def blink(pin):  
	io.output(pin,io.HIGH)  
	time.sleep(2)
	print("Slept first round w/ HIGH")  
	io.output(pin,io.LOW)  
	time.sleep(2)  
	print("Slept second round w/ LOW")
	io.cleanup()

io.setup(32, io.OUT)

config = {
	"apiKey": "AIzaSyDJ31YrXt8JAPUZHYGNRS8WNjoHaz8ssuE",
	"authDomain": "home-b7104.firebaseapp.com",
	"databaseURL": "https://home-b7104.firebaseio.com",
	"storageBucket": "home-b7104.appspot.com"
}

firebase = fb.initialize_app(config)
db = firebase.database()

rooms = db.child("rooms").get()
print(rooms.val())
print("------------------------------------------------------------")
time.sleep(2)
print("I slept")
blink(32)
