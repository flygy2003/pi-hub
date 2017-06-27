import pyrebase as fb

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
